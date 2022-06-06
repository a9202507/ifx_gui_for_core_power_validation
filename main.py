# Rev2022.06.06 for beta release
# a9202507@gmail.com

import sys
from PySide2.QtCore import QThread, Signal
from PySide2.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
import PySide2_DB410_ui
import json
import os
import visa_function as myvisa
import pandas as pd
import DB410_3d_function
import pandas
import time
import pandas_report
import datetime


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

        freq_list_len = len(myWin.parameter_main_freq_list)
        duty_list_len = len(myWin.parameter_main_duty_list)
        measure_result_dict = dict()
        df = pd.DataFrame()
        for freq_idx, freq in enumerate(myWin.parameter_main_freq_list):
            for duty_idx, duty in enumerate(myWin.parameter_main_duty_list):

                self.DB410_msg.emit(f"Freq={str(freq)}, Duty={str(duty)}")
                self.DB410_process_bar.emit(
                    int((duty_idx+freq_idx*duty_list_len)/(freq_list_len*duty_list_len)*100))

                # scope horizontal scale
                myWin.set_horizontal_scale_in_scope(str(1/(freq*1000)))

                myWin.send_function_gen_command_one_time(freq, duty, True)

                # for transinet duration time.
                time.sleep(myWin.parameter_main_ton_duration_time_sec)

                filename = myWin.parameter_setting_filename+str(myWin.parameter_main_high_current)+"A_"+str(
                    myWin.parameter_main_low_current)+"A_"+"Gain"+str(myWin.parameter_main_gain)+"mVa"+"_"+str(freq)+"Khz"+"_D"+str(duty)

                myWin.save_waveform_in_scope(myWin.parameter_setting_folder_in_inst,
                                             filename,
                                             myWin.parameter_setting_filename_include_timestamp
                                             )
                if myWin.debug == True:
                    myWin.push_msg_to_GUI("save_file_to_PC")
                myWin.save_wavefrom_from_scope_to_pc(filename)
                # for save wavefrom delay time
                time.sleep(myWin.parameter_main_ton_duration_time_sec)

                measure_result_dict['item1'] = float(freq)
                measure_result_dict['item2'] = float(duty)
                measure_result_dict['item3'] = float(myWin.get_scope_meansurement_value(
                    3, "value"))
                measure_result_dict['item4'] = float(myWin.get_scope_meansurement_value(
                    4, "value"))
                df = df.append(measure_result_dict, ignore_index=True)
                if myWin.debug == True:
                    self.DB410_msg.emit(str(measure_result_dict))
                    print(f"df={df}")
                time.sleep(0.2)

                myWin.send_function_gen_command_one_time(freq, duty, False)

                # for transient off duration time
                time.sleep(myWin.parameter_main_toff_duration_time_sec)
        self.DB410_process_bar.emit(100)
        df.to_excel(
            f"{myWin.lineEdit_27.text()}/{myWin.lineEdit_7.text()}{myWin.parameter_main_high_current}A_{myWin.parameter_main_low_current}A_report_{datetime.datetime.now().strftime('%Y_%m%d_%H%M')}.xls")

        self.DB410_msg.emit("==3D test finish==")
        self.DB410_msg.emit(" ")

    def stop(self):
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

        # self.pushButton_8.clicked.connect(self.create_visa_equipment)
        self.pushButton_8.clicked.connect(self.run_function_gen_3d_thread)
        self.pushButton_4.clicked.connect(self.stop_function_gen_3d_thread)
        self.pushButton_6.clicked.connect(self.update_equipment_on_combox)
        self.pushButton_5.clicked.connect(self.clear_message_box)
        self.comboBox_2.currentIndexChanged.connect(
            self.update_function_gen_name)
        self.comboBox.currentIndexChanged.connect(
            self.update_escope_name)
        self.pushButton_9.clicked.connect(self.open_3d_report_max)
        self.pushButton_10.clicked.connect(self.open_3d_report_min)

        self.pushButton_7.clicked.connect(
            self.update_GUI_then_save_waveform_once_time)
        self.actionLoad_config.triggered.connect(self.load_config)
        self.actionSave_config.triggered.connect(self.save_config)
        self.actionAbout_the_GUI.triggered.connect(self.about_the_GUI)
        self.about_the_gui_text = "Powered by PySide2 and Python3."
        self.debug = debug
        # set off_RadioButton is checked.
        self.radioButton_2.setChecked(True)
        self.pushButton_11.clicked.connect(self.select_directory)

        # start-up function
        self.update_equipment_on_combox()

        # set auto load init.json during startup
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.path_file_list = list()
        self.path_file_list.append(self.path+"\init.json")
        self.load_config_from_filename(self.path_file_list)

        # functionGen
        self.radioButton.toggled.connect(
            self.update_GUI_then_send_to_function_gen_on)
        self.radioButton_2.toggled.connect(
            self.update_GUI_then_send_to_function_gen_off)

        # initial thread
        self.function_gen_3d = DB410_3d_thread()
        self.function_gen_3d.DB410_msg.connect(self.push_msg_to_GUI)
        self.function_gen_3d.DB410_process_bar.connect(self.set_process_bar)

        # set windowTitle
        Window_title = "IFX loadSlammer GUI Rev.2022.06.06 "

        if self.debug == True:
            self.setWindowTitle(Window_title+"_Debug mode")
        else:
            self.setWindowTitle(Window_title)

    def update_GUI_then_save_waveform_once_time(self):
        self.update_GUI()
        self.save_waveform_in_scope(self.parameter_setting_folder_in_inst,
                                    self.parameter_setting_filename, self.parameter_setting_filename_include_timestamp)
        time.sleep(1)
        self.save_wavefrom_from_scope_to_pc(
            self.waveform_file, self.parameter_setting_filename_include_timestamp)

    def init_scope(self):
        self.scope = myvisa.tek_visa_mso_escope(
            self.parameter_setting_scope_resource_name)

    def save_waveform_in_scope(self, filefolder, filename, timestamp=True):
        self.init_scope()

        # set waveform dirctory in scope
        self.scope.set_waveform_directory_in_scope(self.lineEdit_26.text())

        if timestamp == True:
            dt = datetime.datetime.now()
            timestamp_str = dt.strftime("_%Y%m%d_%H%M%S")
            self.waveform_file = filename+timestamp_str
        else:
            self.waveform_file = filename

        # save waveform
        if self.debug == True:
            self.push_msg_to_GUI(
                f"save waveform as: {filefolder}, {self.waveform_file}")

        self.scope.save_waveform_in_inst(filefolder, self.waveform_file, False)

    def save_wavefrom_from_scope_to_pc(self, filename, timestamp=True):
        local_fildfolder = self.lineEdit_26.text()
        self.scope.save_waveform_back_to_pc(
            local_fildfolder, self.waveform_file+".png", self.lineEdit_27.text()+"/", True)

    def get_scope_meansurement_value(self, item_number=1, measure_item_type="max"):
        result = self.scope.get_measurement_value(
            item_number=item_number, measure_item_type=measure_item_type)
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

    def run_function_gen(self, function_gen_resource_name, high_voltage, low_voltage, freq, duty, rise_time, fall_time, on_off=False):
        self.function_gen = myvisa.tek_visa_functionGen(
            self.comboBox_2.currentText())
        # self.function_gen.set_voltage_high = high_voltage
        # self.function_gen.set_voltage_low = low_voltage
        self.function_gen.set_freq = str(freq)
        self.function_gen.set_duty = str(duty)
        self.function_gen.set_rise_time_ns = str(rise_time)
        self.function_gen.set_fall_time_ns = str(fall_time)
        print(
            f"run_function_gen freq{freq}duty{duty}rise{rise_time}fala{fall_time}")

        if on_off == True:
            self.function_gen.on()
        else:
            self.function_gen.off()

    def update_GUI_then_send_function_gen(self):
        self.update_GUI()
        self.send_function_gen_command_one_time(
            self.lineEdit_8.text(), self.lineEdit_5.text(), self.comboBox_3.currentIndex())

    def update_GUI_then_send_to_function_gen_on(self):
        if self.comboBox_2.currentText() == "":
            QMessageBox.about(
                self, "error", "please select fucntion get on Setting page first")
        else:
            self.update_GUI_then_send_to_function_gen(
                function_output_enable=True)

    def update_GUI_then_send_to_function_gen_off(self):
        if self.comboBox_2.currentText() != "":
            self.update_GUI_then_send_to_function_gen(
                function_output_enable=False)

    def update_GUI_then_send_to_function_gen(self, function_output_enable):
        self.update_GUI()
        self.send_function_gen_command_one_time(self.lineEdit_8.text(
        ), self.lineEdit_5.text(), function_output_enable)

    def send_function_gen_command_one_time(self, freq, duty, on_off=False):
        self.function_gen = myvisa.tek_visa_functionGen(
            self.comboBox_2.currentText())
        self.function_gen.set_duty(duty)
        self.function_gen.set_freq(freq)

        high_voltage_value = float(
            self.lineEdit_16.text())*float(self.lineEdit_17.text())/1000
        low_voltage_value = float(self.lineEdit.text()) * \
            float(self.lineEdit_17.text())/1000
        self.function_gen.set_voltage_high(str(high_voltage_value))
        self.function_gen.set_voltage_low(str(low_voltage_value))
        self.function_gen.set_rise_time_ns(self.lineEdit_6.text())
        self.function_gen.set_fall_time_ns(self.lineEdit_4.text())

        if on_off == True:
            self.function_gen.on()
        else:
            self.function_gen.off()

    def create_visa_equipment(self):
        if self.comboBox.currentText() != "":

            self.escope = myvisa.create_visa_equipment(
                self.comboBox.currentText())
            message = self.escope.query('*IDN?')
            if self.debug == True:
                self.push_msg_to_GUI(message)

    def update_equipment_on_combox(self):
        self.get_visa_resource()
        self.comboBox.clear()
        self.lineEdit_28.clear()
        self.comboBox_2.clear()
        self.lineEdit_29.clear()
        self.comboBox.addItem("")
        self.comboBox.addItems(self.resource_list)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItems(self.resource_list)

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
                               "parameter_setting_scope_resource_name": self.parameter_setting_scope_resource_name,
                               "parameter_setting_function_gen_resource_name": self.parameter_setting_function_gen_resource_name,
                               "parameter_setting_folder_in_inst": self.parameter_setting_folder_in_inst,
                               "parameter_setting_filename": self.parameter_setting_filename,
                               "parameter_setting_filename_include_timestamp": self.parameter_setting_filename_include_timestamp,
                               "parameter_setting_filename_include_transient": self.parameter_setting_filename_include_transient,
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

    def get_filename(self):
        try:
            dlg = QFileDialog(self, 'Open File', '.',
                              'JSON Files (*.json);;XLS Files (*.xls);;All Files (*)')
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

            self.lineEdit_16.setText(
                str(json_data["parameter_main_high_current"]))
            self.lineEdit.setText(str(json_data["parameter_main_low_current"]))
            self.lineEdit_17.setText(str(json_data["parameter_main_gain"]))
            self.lineEdit_6.setText(str(
                json_data["parameter_main_rise_time_nsec"]))
            self.lineEdit_4.setText(str(
                json_data["parameter_main_fall_time_nsec"]))
            self.lineEdit_5.setText(str(json_data["parameter_main_duty"]))
            self.lineEdit_8.setText(str(json_data["parameter_main_frequency"]))
            # =============================
            self.lineEdit_13.setText(
                str(json_data["parameter_main_duty_list"])[1:-1])
            self.lineEdit_15.setText(
                str(json_data["parameter_main_freq_list"])[1:-1])
            self.lineEdit_21.setText(str(
                json_data["parameter_main_ton_duration_time_sec"]))
            self.lineEdit_22.setText(str(
                json_data["parameter_main_toff_duration_time_sec"]))
            self.checkBox_3.setChecked(
                json_data["parameter_main_roll_up_down_enable"])
            # ==================================
            self.lineEdit_26.setText(
                json_data["parameter_setting_folder_in_inst"])
            self.lineEdit_7.setText(
                str(json_data["parameter_setting_filename"]))
            self.checkBox_2.setChecked(
                json_data["parameter_setting_filename_include_timestamp"])

    def about_the_GUI(self):
        QMessageBox.about(self, "about the GUI", self.about_the_gui_text)

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
        self.parameter_main_duty_list = eval(
            "["+str(self.lineEdit_13.text())+"]")

        self.parameter_main_freq_list = eval(
            "["+str(self.lineEdit_15.text())+"]")
        self.parameter_main_ton_duration_time_sec = float(
            self.lineEdit_21.text())
        self.parameter_main_toff_duration_time_sec = float(
            self.lineEdit_22.text())
        self.parameter_main_roll_up_down_enable = self.checkBox_3.isChecked()

        # setting page
        self.parameter_setting_function_gen_resource_name = self.comboBox_2.currentText()
        self.parameter_setting_scope_resource_name = self.comboBox.currentText()
        self.parameter_setting_folder_in_inst = self.lineEdit_26.text()
        self.parameter_setting_filename = self.lineEdit_7.text()
        self.parameter_setting_filename_include_timestamp = self.checkBox_2.isChecked()
        self.parameter_setting_filename_include_transient = self.checkBox.isChecked()

    def update_function_gen_name(self):
        if self.comboBox_2.currentText() != "":
            self.function_gen = myvisa.tek_visa_functionGen(
                self.comboBox_2.currentText())
            device_name = self.function_gen.get_equipment_name()
            self.lineEdit_29.setText(device_name)

    def update_escope_name(self):
        if self.comboBox.currentText() != "":
            self.function_gen = myvisa.tek_visa_functionGen(
                self.comboBox.currentText())
            device_name = self.function_gen.get_equipment_name()
            self.lineEdit_28.setText(device_name)

    def set_horizontal_scale_in_scope(self, scale_value="1e-6"):
        self.scope.set_horizontal_scale(scale_value)

    def clear_message_box(self):
        self.textEdit.clear()

    def open_3d_report_max(self):
        self.get_filename()
        print(self.filenames[0])
        pandas_report.plt_vmax(self.filenames[0])

    def open_3d_report_min(self):
        self.get_filename()
        print(self.filenames[0])
        pandas_report.plt_vmin(self.filenames[0])

    def select_directory(self):
        self.dir_path = QFileDialog.getExistingDirectory(
            self, "Chose Directory", "./")
        self.lineEdit_27.setText(self.dir_path)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWin = MyMainWindow(debug=False)

    myWin.show()

    sys.exit(app.exec_())
