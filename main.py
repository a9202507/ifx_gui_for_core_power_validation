# Rev2024.02.01 for beta release
# a9202507@gmail.com

import sys
from PySide2.QtCore import QThread, Signal
from PySide2.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PySide2.QtGui import QIcon
import PySide2_DB410_ui
import json
import os
import visa_function as myvisa
import pandas as pd
import DB410_3d_function
import time
import pandas_report
import datetime

# set icon to taskbar
import ctypes
myappid = 'mycompany.myproduct.subproduct.version'  # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class DB410_3d_thread(QThread):
    DB410_msg = Signal(str)
    DB410_process_bar = Signal(int)

    def __init__(self):
        QThread.__init__(self)

        # self.DB410_msg = Signal(str)

    def __del__(self):
        self.wait()

    def run(self):
        self.DB410_msg.emit("== start to run 3D test==")
        myWin.update_GUI()
        myWin.init_scope()
        myWin.init_function_gen()

        freq_list_len = len(myWin.parameter_main_freq_list)
        duty_list_len = len(myWin.parameter_main_duty_list)
        measure_result_dict = dict()
        df = pd.DataFrame()

        # setup measurement items in escope
        vout_channel = myWin.comboBox_3.currentText()
        iout_channel = myWin.comboBox_4.currentText()
        myWin.set_scope_measurement_item(1, vout_channel, 'max')
        myWin.set_scope_measurement_item(2, vout_channel, 'min')
        myWin.set_scope_measurement_item(3, vout_channel, 'pkpk')
        myWin.set_scope_measurement_item(4, iout_channel, 'frequency')
        myWin.set_scope_measurement_item(5, iout_channel, 'duty')
        myWin.set_scope_measurement_item(6, iout_channel, 'max')
        myWin.set_scope_measurement_item(7, iout_channel, 'min')

        for freq_idx, freq in enumerate(myWin.parameter_main_freq_list):
            for duty_idx, duty in enumerate(myWin.parameter_main_duty_list):

                self.DB410_msg.emit(f"Freq={str(freq)}, Duty={str(duty)}")
                self.DB410_process_bar.emit(
                    int((duty_idx+freq_idx*duty_list_len)/(freq_list_len*duty_list_len)*100))

                # send function generator on command
                myWin.send_function_gen_command_one_time(freq, duty, True)

                # scope start acquisition, set trigger and horizontal scale, reset statistics
                myWin.scope.acq_run()
                time.sleep(0.5)
                myWin.scope.set_trigger(iout_channel, "auto", "DC")
                myWin.set_horizontal_scale_in_scope(str(1/(freq*1000)))
                myWin.scope.reset_statistics()

                # sleep for transient on duration time
                time.sleep(myWin.parameter_main_ton_duration_time_sec)

                # stop acquisition
                myWin.scope.acq_stop()
                time.sleep(1.5) # delay to allow scope to update screen with latest values after stopping
                
                # get measurements
                measure_result_dict['Freq'] = float(freq)
                measure_result_dict['duty'] = float(duty)
                vmax = myWin.get_scope_measurement_statistics(item_number=1, channel=vout_channel, item_type="max", item_statistic="max")
                if myWin.debug == True:
                    myWin.push_msg_to_GUI(f"line88 vmax={vmax}")
                measure_result_dict['Vmax'] = float(vmax)

                #
                # except:
                #    myWin.push_msg_to_GUI(f"Failed to get measurement from scope , Vmax={vmax}")

                vmin = myWin.get_scope_measurement_statistics(item_number=2, channel=vout_channel, item_type="min", item_statistic="min")
                if myWin.debug == True:
                    myWin.push_msg_to_GUI(f"line97 vmin={vmin}")
                measure_result_dict['Vmin'] = float(vmin)

                #
                # except:
                #    myWin.push_msg_to_GUI(f"Failed to get measurement from scope , Vmin={vmin}")

                df = pd.concat([df, pd.DataFrame([measure_result_dict])], ignore_index=True)

                if myWin.debug == True:
                    self.DB410_msg.emit(str(measure_result_dict))
                    print(f"df={df}")

                # get screenshot
                if myWin.parameter_setting_filename_include_timestamp == True:
                    dt = datetime.datetime.now()
                    timestamp_str = dt.strftime("_%Y-%m-%d_%H%M%S")
                else:
                    timestamp_str = ""
                filename = f"{myWin.parameter_setting_filename}{myWin.parameter_main_high_current}A_{myWin.parameter_main_low_current}A_{freq}kHz_D{duty}{timestamp_str}"

                if myWin.debug == True:
                    myWin.push_msg_to_GUI("save file to scope and PC")
                    myWin.push_msg_to_GUI(f"line65 filename = {filename}")
                try:
                    myWin.save_waveform_in_scope_and_pc(filename)
                except:
                    myWin.push_msg_to_GUI("Failed to save waveform")

                # send function generator off command
                myWin.function_gen_off()

                # sleep for for transient off duration time
                time.sleep(myWin.parameter_main_toff_duration_time_sec)

        self.DB410_process_bar.emit(100)

        # save report file
        if myWin.parameter_setting_filename_include_timestamp == True:
            dt = datetime.datetime.now()
            timestamp_str = dt.strftime("_%Y-%m-%d_%H%M%S")
        else:
            timestamp_str = ""
        try:
            df.to_excel(f"{myWin.parameter_setting_local_folder}/{myWin.parameter_setting_filename}{myWin.parameter_main_high_current}A_{myWin.parameter_main_low_current}A_report{timestamp_str}.xlsx")
        except:
            myWin.push_msg_to_GUI("Failed to save report to PC")
        self.DB410_msg.emit("==3D test finish==")
        self.DB410_msg.emit(" ")

    def stop(self):
        myWin.function_gen_off()
        self.DB410_msg.emit("==3D test stop==")
        self.DB410_msg.emit(" ")
        self.DB410_process_bar.emit(0)
        # todo
        self.terminate()


class MyMainWindow(QMainWindow, PySide2_DB410_ui.Ui_MainWindow):
    def __init__(self, parent=None, debug=False):
        super(MyMainWindow, self).__init__(parent)
        self.setFixedSize(730, 850)
        self.setupUi(self)

        self.pushButton_8.clicked.connect(self.run_function_gen_3d_thread)
        self.pushButton_4.clicked.connect(self.stop_function_gen_3d_thread)
        self.pushButton_6.clicked.connect(self.update_equipment_address_on_combobox)
        self.pushButton_5.clicked.connect(self.clear_message_box)
        self.comboBox.currentIndexChanged.connect(self.update_scope_address)
        self.comboBox_6.currentIndexChanged.connect(self.update_scope_address)
        self.comboBox_2.currentIndexChanged.connect(self.update_function_gen_address)
        self.comboBox_7.currentIndexChanged.connect(self.update_function_gen_address)
        self.pushButton_9.clicked.connect(self.open_3d_report_max)
        self.pushButton_10.clicked.connect(self.check_debug_mode)

        self.pushButton_7.clicked.connect(lambda: self.update_GUI_then_save_waveform("temp"))
        self.pushButton_7.setEnabled(False)

        self.actionLoad_config.triggered.connect(self.load_config)
        self.actionSave_config.triggered.connect(self.save_config)
        self.actionAbout_the_GUI.triggered.connect(self.about_the_gui)

        self.debug = debug
        # set off_RadioButton is checked.
        self.radioButton_2.setChecked(True)
        self.pushButton_11.clicked.connect(self.select_directory)

        # start-up function
        self.update_equipment_address_on_combobox()
        self.update_equipment_type_on_combobox()

        # set auto load init.json during startup
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.path_file_list = list()
        self.path_file_list.append(self.path+"\init.json")
        self.load_config_from_filename(self.path_file_list)

        # functionGen
        self.radioButton.toggled.connect(self.update_GUI_then_send_to_function_gen_on)
        self.radioButton_2.toggled.connect(self.update_GUI_then_send_to_function_gen_off)

        # initial thread
        self.function_gen_3d = DB410_3d_thread()
        self.function_gen_3d.DB410_msg.connect(self.push_msg_to_GUI)
        self.function_gen_3d.DB410_process_bar.connect(self.set_process_bar)
        self.set_process_bar(0)

        # set windowTitle
        self.Window_title = "Infineon GUI for core power validation, Rev.2024.02.01"

        # set icon
        app_icon = QIcon()
        app_icon.addFile("./resource/load slammer.ico")
        self.setWindowIcon(app_icon)

        self.set_window_title_with_debug_mode()

        self.set_components_order()

    def set_components_order(self):
        self.setTabOrder(self.lineEdit_16, self.lineEdit)
        self.setTabOrder(self.lineEdit, self.lineEdit_17)
        self.setTabOrder(self.lineEdit_17, self.lineEdit_6)
        self.setTabOrder(self.lineEdit_6, self.lineEdit_4)
        self.setTabOrder(self.lineEdit_4, self.lineEdit_5)
        self.setTabOrder(self.lineEdit_5, self.lineEdit_8)
        self.setTabOrder(self.lineEdit_8, self.radioButton_2)
        self.setTabOrder(self.radioButton_2, self.radioButton)
        self.setTabOrder(self.radioButton, self.lineEdit_13)
        self.setTabOrder(self.lineEdit_13, self.lineEdit_15)
        self.setTabOrder(self.lineEdit_15, self.lineEdit_21)
        self.setTabOrder(self.lineEdit_21, self.lineEdit_22)
        #self.setTabOrder(self.lineEdit_22, self.lineEdit_16)

    def set_window_title_with_debug_mode(self):
        if self.debug == True:
            self.setWindowTitle(self.Window_title+"_Debug mode")
        else:
            self.setWindowTitle(self.Window_title)

    def check_debug_mode(self):
        self.update_GUI()
        self.init_scope()
        self.set_window_title_with_debug_mode()

        if self.lineEdit_7.text() == "53523962":
            self.set_debug_mode_enable(True)
            self.push_msg_to_GUI(f"debug is {self.debug}")
        else:
            self.set_debug_mode_enable(False)
        self.pushButton_7.setEnabled(True)

    def set_debug_mode_enable(self, mode=False):
        self.debug = mode
        self.set_window_title_with_debug_mode()


    def init_scope(self):
        self.scope = myvisa.scope_types[self.parameter_setting_scope_resource_type](self.parameter_setting_scope_resource_address)

    def init_function_gen(self):
        self.function_gen = myvisa.function_gen_types[self.parameter_setting_function_gen_resource_type](self.parameter_setting_function_gen_resource_address)
        self.function_gen.set_output_impedance("HiZ")
        self.function_gen.set_waveform_shape("pulse")
 
    def update_GUI_then_save_waveform(self, filename="temp"):
        self.update_GUI()
        self.save_waveform_in_scope_and_pc(filename)

    def save_waveform_in_scope_and_pc(self, filename="temp"):
        #self.init_scope()
        
        # set waveform dirctory in scope
        #self.scope.set_waveform_directory_in_scope(self.parameter_setting_scope_folder)

        #self.latest_waveform_filename = filename

        # save waveform to scope
        if self.debug == True:
            self.push_msg_to_GUI(f"save waveform as: {self.parameter_setting_scope_folder}/{filename}")
        self.scope.save_waveform(self.parameter_setting_scope_folder, filename, self.parameter_setting_local_folder, self.debug)

    def set_scope_measurement_item(self, item_number=1, channel="1", item_type="max"):
        result = self.scope.set_measurement_items(item_number, channel, item_type)
        return result

    def get_scope_measurement_statistics(self, item_number=1, channel="1", item_type="max", item_statistic="mean"):
        result = self.scope.get_measurement_statistics(item_number, channel, item_type, item_statistic)
        return result

    def get_scope_measurement_value(self, item_number=1, channel="1", item_type="max"):
        result = self.scope.get_measurement_value(item_number, channel, item_type)
        return result

    def set_process_bar(self, data):
        self.progressBar.setValue(data)

    def run_function_gen_3d_thread(self):
        # self.push_msg_to_GUI("run function gen 3d")
        self.update_GUI()
        if self.comboBox_2.currentText() == "" or self.comboBox.currentText() == "":
            QMessageBox.about(
                self, "error", "please check equipment setting on Setting page")
        else:
            self.function_gen_3d.start()
        # self.myprogpressbar.start()

    def stop_function_gen_3d_thread(self):
        self.function_gen_3d.stop()
        # self.push_msg_to_GUI("stop the 3d test")

    '''def run_function_gen(self, function_gen_resource_name, high_voltage, low_voltage, freq, duty, rise_time, fall_time, on_off=False):
        self.function_gen = myvisa.tek_visa_functionGen(
            self.comboBox_2.currentText())
        # self.function_gen.set_voltage_high = high_voltage
        # self.function_gen.set_voltage_low = low_voltage

        # set ouput inpedance to high-z
        self.function_gen.set_output_impedance(impedance_value="HiZ")
        print("output_impedance")
        self.function_gen.set_freq = str(freq)
        self.function_gen.set_duty = str(duty)
        self.function_gen.set_rise_time_ns = str(rise_time)
        self.function_gen.set_fall_time_ns = str(fall_time)

        if self.debug == True:
            print(
                f"run_function_gen freq{freq}duty{duty}rise{rise_time}fala{fall_time}")

        if on_off == True:
            self.function_gen.on()
        else:
            self.function_gen.off()'''

    def update_GUI_then_send_to_function_gen_on(self):
        if self.comboBox_2.currentText() == "":
            QMessageBox.about(
                self, "error", "please select function gen on Setting page first")
        else:
            # only execute if on button is checked (otherwise, command will be sent twice)
            if self.radioButton.isChecked() == True:
                self.update_GUI_then_send_to_function_gen(function_output_enable=True)

    def update_GUI_then_send_to_function_gen_off(self):
        if self.comboBox_2.currentText() != "":
            # only execute if off button is checked (otherwise, command will be sent twice)
            if self.radioButton_2.isChecked() == True:
                self.update_GUI_then_send_to_function_gen(function_output_enable=False)

    def function_gen_off(self):
        self.function_gen.off()

    def update_GUI_then_send_to_function_gen(self, function_output_enable):
        self.update_GUI()
        self.send_function_gen_command_one_time(self.parameter_main_frequency, self.parameter_main_duty, function_output_enable)

    def send_function_gen_command_one_time(self, freq, duty, on_off=False):
        if on_off == False:
            self.function_gen.off()
        self.function_gen.set_freq(freq)
        self.function_gen.set_duty(duty)
        high_voltage_value = float(self.parameter_main_high_current) * float(self.parameter_main_gain) / 1000
        low_voltage_value = float(self.parameter_main_low_current) * float(self.parameter_main_gain) / 1000
        self.function_gen.set_voltage_high(str(high_voltage_value))
        self.function_gen.set_voltage_low(str(low_voltage_value))
        self.function_gen.set_rise_time_ns(self.parameter_main_rise_time_nsec)
        self.function_gen.set_fall_time_ns(self.parameter_main_fall_time_nsec)
        if on_off == True:
            self.function_gen.on()

    def update_equipment_address_on_combobox(self):
        self.get_visa_resource()
        self.comboBox.clear()
        self.lineEdit_28.clear()
        self.comboBox_2.clear()
        self.lineEdit_29.clear()
        self.comboBox.addItem("")
        self.comboBox.addItems(self.resource_list)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItems(self.resource_list)

    def update_equipment_type_on_combobox(self):
        self.comboBox_6.clear()
        self.comboBox_7.clear()
        # use the keys of the equipment type dictionaries to create the equipment list
        self.comboBox_6.addItems(list(myvisa.scope_types.keys()))
        self.comboBox_7.addItems(list(myvisa.function_gen_types.keys()))
    
    def get_visa_resource(self):

        self.resource_list = myvisa.get_visa_resource_list(
            not self.debug)
        if self.debug == True:
            self.push_msg_to_GUI(self.resource_list)

    def push_msg_to_GUI(self, msg=""):
        if True:
            self.textEdit.append(str(msg))
            # self.textEdit.append("")
        else:
            pass

    def save_config(self):
        self.update_GUI()
        self.parameter_dict = {"parameter_main_high_current": self.parameter_main_high_current,
                               "parameter_main_low_current": self.parameter_main_low_current,
                               "parameter_main_gain": self.parameter_main_gain,
                               "parameter_main_rise_time_nsec": self.parameter_main_rise_time_nsec,
                               "parameter_main_fall_time_nsec": self.parameter_main_fall_time_nsec,
                               "parameter_main_duty": self.parameter_main_duty,
                               "parameter_main_frequency": self.parameter_main_frequency,
                               # ===========================================================
                               "parameter_main_duty_list": self.parameter_main_duty_list,
                               "parameter_main_freq_list": self.parameter_main_freq_list,
                               "parameter_main_ton_duration_time_sec": self.parameter_main_ton_duration_time_sec,
                               "parameter_main_toff_duration_time_sec": self.parameter_main_toff_duration_time_sec,
                               "parameter_main_roll_up_down_enable": self.parameter_main_roll_up_down_enable,
                               # ===========================================================
                               "parameter_setting_scope_resource_type": self.parameter_setting_scope_resource_type,
                               "parameter_setting_scope_resource_address": self.parameter_setting_scope_resource_address,
                               "parameter_setting_function_gen_resource_type": self.parameter_setting_function_gen_resource_type,
                               "parameter_setting_function_gen_resource_address": self.parameter_setting_function_gen_resource_address,
                               "parameter_setting_scope_folder": self.parameter_setting_scope_folder,
                               "parameter_setting_local_folder": self.parameter_setting_local_folder,
                               "parameter_setting_filename": self.parameter_setting_filename,
                               "parameter_setting_screenshot_save_scope": self.parameter_setting_screenshot_save_scope,
                               "parameter_setting_screenshot_save_pc": self.parameter_setting_screenshot_save_pc,
                               "parameter_setting_filename_include_timestamp": self.parameter_setting_filename_include_timestamp,
                               "parameter_setting_scope_vout_channel": self.parameter_setting_scope_vout_channel,
                               "parameter_setting_scope_iout_channel": self.parameter_setting_scope_iout_channel,
                               "parameter_setting_function_gen_channel": self.parameter_setting_function_gen_channel,
                               }
        filename_with_path = QFileDialog.getSaveFileName(
            self, 'Save File', '.', 'JSON Files (*.json)')
        save_filename = filename_with_path[0]
        if save_filename != "":
            with open(save_filename, 'w') as fp:
                # json.dump(self.parameter_dict, fp)
                fp.write(json.dumps(self.parameter_dict, indent=4))

        if self.debug == True:
            self.push_msg_to_GUI(self.parameter_dict)

    def load_config(self):

        self.get_filename()
        # print(self.filenames[0])
        self.load_config_from_filename(self.filenames)

    def get_filename(self, filetype='JSON Files (*.json);;XLS Files (*.xls);;All Files (*)'):
        try:
            dlg = QFileDialog(self, 'Open File', '.', filetype)
            if dlg.exec_():
                self.filenames = dlg.selectedFiles()
                if self.debug == True:
                    self.push_msg_to_GUI(self.filenames)

        except:
            QMessageBox.about(self, "Warning", "the filename isn't work")

    def load_config_from_filename(self, filenames):

        with open(filenames[0], 'r') as j:
            json_data = json.load(j)
            if self.debug == True:
                self.push_msg_to_GUI(str(json_data))

            self.lineEdit_16.setText(str(json_data["parameter_main_high_current"]))
            self.lineEdit.setText(str(json_data["parameter_main_low_current"]))
            self.lineEdit_17.setText(str(json_data["parameter_main_gain"]))
            self.lineEdit_6.setText(str(json_data["parameter_main_rise_time_nsec"]))
            self.lineEdit_4.setText(str(json_data["parameter_main_fall_time_nsec"]))
            self.lineEdit_5.setText(str(json_data["parameter_main_duty"]))
            self.lineEdit_8.setText(str(json_data["parameter_main_frequency"]))
            # =============================
            self.lineEdit_13.setText(str(json_data["parameter_main_duty_list"])[1:-1])
            self.lineEdit_15.setText(str(json_data["parameter_main_freq_list"])[1:-1])
            self.lineEdit_21.setText(str(json_data["parameter_main_ton_duration_time_sec"]))
            self.lineEdit_22.setText(str(json_data["parameter_main_toff_duration_time_sec"]))
            self.checkBox_3.setChecked(json_data["parameter_main_roll_up_down_enable"])
            # ==================================
            self.lineEdit_26.setText(json_data["parameter_setting_scope_folder"])
            self.lineEdit_27.setText(json_data["parameter_setting_local_folder"])
            self.lineEdit_7.setText(str(json_data["parameter_setting_filename"]))
            self.checkBox_4.setChecked(json_data["parameter_setting_screenshot_save_scope"])
            self.checkBox_5.setChecked(json_data["parameter_setting_screenshot_save_pc"])
            self.checkBox_2.setChecked(json_data["parameter_setting_filename_include_timestamp"])
            self.comboBox_3.setCurrentText(json_data["parameter_setting_scope_vout_channel"])
            self.comboBox_4.setCurrentText(json_data["parameter_setting_scope_iout_channel"])
            self.comboBox_5.setCurrentText(json_data["parameter_setting_function_gen_channel"])
            self.comboBox_6.setCurrentText(json_data["parameter_setting_scope_resource_type"])
            self.comboBox.setCurrentText(json_data["parameter_setting_scope_resource_address"])
            self.comboBox_7.setCurrentText(json_data["parameter_setting_function_gen_resource_type"])
            self.comboBox_2.setCurrentText(json_data["parameter_setting_function_gen_resource_address"])
            
    def update_GUI(self):
        # get GUI import
        # main page
        self.parameter_main_high_current = float(self.lineEdit_16.text())
        self.parameter_main_low_current = float(self.lineEdit.text())
        self.parameter_main_gain = float(self.lineEdit_17.text())
        self.parameter_main_rise_time_nsec = float(self.lineEdit_6.text())
        self.parameter_main_fall_time_nsec = float(self.lineEdit_4.text())
        self.parameter_main_duty = float(self.lineEdit_5.text())
        self.parameter_main_frequency = float(self.lineEdit_8.text())

        # ======
        self.parameter_main_duty_list = eval("["+str(self.lineEdit_13.text())+"]")

        self.parameter_main_freq_list = eval("["+str(self.lineEdit_15.text())+"]")
        self.parameter_main_ton_duration_time_sec = float(self.lineEdit_21.text())
        self.parameter_main_toff_duration_time_sec = float(self.lineEdit_22.text())
        self.parameter_main_roll_up_down_enable = self.checkBox_3.isChecked()

        # setting page
        self.parameter_setting_function_gen_resource_type = self.comboBox_7.currentText()
        self.parameter_setting_function_gen_resource_address = self.comboBox_2.currentText()
        self.parameter_setting_scope_resource_type = self.comboBox_6.currentText()
        self.parameter_setting_scope_resource_address = self.comboBox.currentText()
        self.parameter_setting_scope_folder = self.lineEdit_26.text()
        self.parameter_setting_local_folder = self.lineEdit_27.text()
        self.parameter_setting_filename = self.lineEdit_7.text()
        self.parameter_setting_screenshot_save_scope = self.checkBox_4.isChecked()
        self.parameter_setting_screenshot_save_pc = self.checkBox_5.isChecked()
        self.parameter_setting_filename_include_timestamp = self.checkBox_2.isChecked()
        self.parameter_setting_scope_vout_channel = self.comboBox_3.currentText()
        self.parameter_setting_scope_iout_channel = self.comboBox_4.currentText()
        self.parameter_setting_function_gen_channel = self.comboBox_5.currentText()
        
    def update_scope_address(self):
        if self.comboBox.currentText() != "":
            self.update_GUI()
            self.init_scope()
            self.lineEdit_28.setText(self.scope.get_equipment_name())

    def update_function_gen_address(self):
        if self.comboBox_2.currentText() != "":
            self.update_GUI()
            self.init_function_gen()
            self.lineEdit_29.setText(self.function_gen.get_equipment_name())

    def set_horizontal_scale_in_scope(self, scale_value="1e-6"):
        self.scope.set_horizontal_scale(scale_value)

    def clear_message_box(self):
        self.textEdit.clear()

    def open_3d_report_max(self):
        self.get_filename(filetype="Excel Files (*.xls; *.xlsx)")

        if self.debug == True:
            print(self.filenames[0])
        pandas_report.plt_vmax(self.filenames[0])

    def select_directory(self):
        self.dir_path = QFileDialog.getExistingDirectory(
            self, "Chose Directory", "./")
        self.lineEdit_27.setText(self.dir_path)

    def about_the_gui(self):
        QMessageBox.about(
            self, "About the GUI", 'Powered by PySide2, <a href=https://github.com/a9202507/ifx_loadslammer>Github</a>')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWin = MyMainWindow(debug=False)

    myWin.show()

    sys.exit(app.exec_())
