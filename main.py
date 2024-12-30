# a9202507@gmail.com
# christian.berger@infineon.com

import sys
from PySide6.QtCore import QThread, Signal, Slot,Qt,QEvent
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox,QLineEdit,QVBoxLayout,QPushButton,QDialog
from PySide6.QtGui import QIcon, QPixmap,QPalette, QColor,QDoubleValidator
import PySide6_Core_Power_Validation_ui
import json
import os
import visa_function as myvisa
import pandas as pd
import DB410_3d_function
import time
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas_report
import datetime
import webbrowser

basedir = os.path.dirname(__file__)

# set icon to taskbar (only exists on windows)
try:
    from ctypes import windll
    myappid = 'com.infineon.GUI.corepowervalidation.20241230'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass


class DB410_3d_thread(QThread):
    DB410_msg = Signal(str)
    DB410_progress_bar = Signal(int)
    DB410_open_3d_plot = Signal(str)

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
                self.DB410_progress_bar.emit(
                    int((duty_idx+freq_idx*duty_list_len)/(freq_list_len*duty_list_len)*100))

                # send function generator on command
                myWin.send_function_gen_command_one_time(freq, duty, True)

                # scope start acquisition, set trigger and horizontal scale, reset statistics
                myWin.scope.acq_run()
                time.sleep(0.25)
                #myWin.scope.set_trigger(iout_channel, "auto", "DC")
                myWin.set_horizontal_scale_in_scope(str(1/(freq*1000)))
                time.sleep(0.25)
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
                
                if myWin.checkBox_7.isChecked():
                    if myWin.debug==True:
                        myWin.push_msg_to_GUI("save Tek session file to scope")
                        myWin.push_msg_to_GUI(f"filename:{filename}.tss")
                    try:
                        myWin.scope.save_session(scope_folder='C:/temp/',filename=filename)
                    except:
                        myWin.push_msg_to_GUI("failed to save session")

                # send function generator off command
                myWin.function_gen.off(myWin.parameter_setting_function_gen_channel)

                # sleep for for transient off duration time
                time.sleep(myWin.parameter_main_toff_duration_time_sec)

        self.DB410_progress_bar.emit(100)

        # save report file
        if myWin.parameter_setting_filename_include_timestamp == True:
            dt = datetime.datetime.now()
            timestamp_str = dt.strftime("_%Y-%m-%d_%H%M%S")
        else:
            timestamp_str = ""
        filename = f"{myWin.parameter_setting_local_folder}/{myWin.parameter_setting_filename}{myWin.parameter_main_high_current}A_{myWin.parameter_main_low_current}A_report{timestamp_str}.xlsx"
        try:
            with pd.ExcelWriter(filename, mode="w") as writer:
                df.to_excel(writer,sheet_name="row")
                df.sort_values(by='Vmax',ascending=False).to_excel(writer, sheet_name="Vmax")
                df.sort_values(by='Vmin').to_excel(writer, sheet_name="Vmin")
                #df.to_excel(filename,sheet_name="ROW") # save to ROW sheet without sort
                #df.sort_values(by='Vmax',ascending=False).to_excel(filename,sheet_name="Vmax") # sort by Vmax and save to Vmax sheet
                #df.sort_values(by="Vmin").to_excel(filename,sheet_name="Vmin") # sort by Vmin and save to Vmin sheet.
                if myWin.parameter_setting_autocreate_3d_plot == True:
                    self.DB410_open_3d_plot.emit(filename)
        except:
            myWin.push_msg_to_GUI("Failed to save report to PC")
        self.DB410_msg.emit("==3D test finish==")
        self.DB410_msg.emit(" ")

    def stop(self):
        myWin.function_gen.off(myWin.parameter_setting_function_gen_channel)
        self.DB410_msg.emit("==3D test stop==")
        self.DB410_msg.emit(" ")
        self.DB410_progress_bar.emit(0)
        # todo
        self.terminate()


class MyMainWindow(QMainWindow, PySide6_Core_Power_Validation_ui.Ui_MainWindow):
    def __init__(self, parent=None, debug=False):
        super(MyMainWindow, self).__init__(parent)
        self.setFixedSize(1050, 700)
        self.setupUi(self)

        self.pushButton_8.clicked.connect(self.run_function_gen_3d_thread)
        self.pushButton_4.clicked.connect(self.stop_function_gen_3d_thread)
        self.pushButton_6.clicked.connect(self.update_equipment_address_on_combobox)
        self.pushButton_5.clicked.connect(self.clear_message_box)
        self.comboBox.currentIndexChanged.connect(self.update_scope_address)
        self.comboBox_6.currentIndexChanged.connect(self.update_scope_address)
        self.comboBox_2.currentIndexChanged.connect(self.update_function_gen_address)
        self.comboBox_7.currentIndexChanged.connect(self.update_function_gen_address)
        self.pushButton_9.clicked.connect(self.open_3d_plot)
        self.pushButton_10.clicked.connect(self.set_debug_mode_enable)
        self.lineEdit.editingFinished.connect(self.update_GUI)
        self.lineEdit_16.editingFinished.connect(self.update_GUI)
        self.lineEdit_6.editingFinished.connect(self.update_GUI)
        self.lineEdit_4.editingFinished.connect(self.update_GUI)

        self.label_7.setText("Freq(Khz)(up/down)")
        self.label_12.setText("Toggle (Q)/(Space)")

        # auto on/off function generator when paramters chagned.
        self.lineEdit_16.editingFinished.connect(self.auto_on_off_function_gen_when_parameters_changed)
        self.lineEdit_17.editingFinished.connect(self.auto_on_off_function_gen_when_parameters_changed)
        self.lineEdit.editingFinished.connect(self.auto_on_off_function_gen_when_parameters_changed)
        self.lineEdit_6.editingFinished.connect(self.auto_on_off_function_gen_when_parameters_changed)
        self.lineEdit_4.editingFinished.connect(self.auto_on_off_function_gen_when_parameters_changed)
        self.lineEdit_5.editingFinished.connect(self.auto_on_off_function_gen_when_parameters_changed)
        self.lineEdit_8.editingFinished.connect(self.auto_on_off_function_gen_when_parameters_changed)
        self.lineEdit_8.textChanged.connect(self.lineedit_update_to_slider)
        


        self.pushButton_7.clicked.connect(self.update_GUI_then_save_waveform_once_time)
        #self.pushButton_7.setEnabled(False)

        # generate 1K to 1000K step 2K frequency list for user.
        self.pushButton_12.clicked.connect(self.update_frequency_list_on_gui)


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

        # auto load init.json during startup - for packaged .exe, init.json in same folder as .exe will be used, if it exists - otherwise default init.json.
        self.configfile_list = list()
        if os.path.isfile("./init.json"):
            self.configfile_list.append("./init.json")
        else:
            self.configfile_list.append(f"{basedir}/init.json")
        self.load_config_from_filename(self.configfile_list)

        # functionGen
        self.radioButton.toggled.connect(self.update_GUI_then_send_to_function_gen_on)
        self.radioButton_2.toggled.connect(self.update_GUI_then_send_to_function_gen_off)

        # initial thread
        self.function_gen_3d = DB410_3d_thread()
        self.function_gen_3d.DB410_msg.connect(self.push_msg_to_GUI)
        self.function_gen_3d.DB410_progress_bar.connect(self.set_progress_bar)
        self.function_gen_3d.DB410_open_3d_plot.connect(lambda filename: self.open_3d_plot(filename))
        self.set_progress_bar(0)

        # slew rate and rise time/fall time calculation
        self.lineEdit_16.editingFinished.connect(self.update_GUI)
        self.lineEdit.editingFinished.connect(self.update_GUI)
        self.lineEdit_6.editingFinished.connect(self.update_rise_time)
        self.lineEdit_9.editingFinished.connect(self.update_rise_slew_rate)
        self.lineEdit_4.editingFinished.connect(self.update_fall_time)
        self.lineEdit_10.editingFinished.connect(self.update_fall_slew_rate)
        self.horizontalSlider.valueChanged.connect(self.slider_update_to_lineedit)

        # set windowTitle
        self.Window_title = "Infineon GUI for core power validation, Rev. 2024-12-30"

        # set icon
        app_icon = QIcon()
        app_icon.addFile(f"{basedir}/resource/load_slammer.ico")
        self.setWindowIcon(app_icon)
        
        # set IFX logo
        self.label_10.setPixmap(QPixmap(f"{basedir}/resource/IFX_LOGO_RGB.jpg"))

        # click logo then open brower.
        self.label_10.setCursor(Qt.PointingHandCursor)
        self.label_10.mousePressEvent = self.label_click_event

        self.set_window_title_with_debug_mode()


        # 創建自定義滑塊
        
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(1000)
        self.horizontalSlider.setValue(1)


        self.set_components_order()

    def lineedit_update_to_slider(self,value):
        self.horizontalSlider.setValue(int(self.lineEdit_8.text()))

    def slider_update_to_lineedit(self,value):
        if self.debug:
            self.push_msg_to_GUI(f"freq={value}Khz")
        self.lineEdit_8.setText(str(value))
        self.auto_on_off_function_gen_when_parameters_changed()

    def label_click_event(self, event):
        if event.button() == Qt.LeftButton:
            webbrowser.open('https://softwaretools.infineon.com/tools/com.ifx.tb.tool.infineonguiforcorepowervalidation')

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Confirmation', 
                                     'Are you sure you want to quit?',
                                     QMessageBox.Yes | QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            # turn off AFG before close GUI.
            self.update_GUI_then_send_to_function_gen(function_output_enable=False)
            event.accept()
        else:
            event.ignore()
    @Slot()
    def update_rise_time(self):
        high_current=float(self.lineEdit_16.text())
        low_current=float(self.lineEdit.text())
        current_step=high_current-low_current
        value=float(self.lineEdit_6.text())
        rise_time=round( (0.8*current_step/value)*1000 , 1)
        self.lineEdit_9.setText(str(rise_time))
        #self.push_msg_to_GUI(f"1 rise_time={rise_time},slew_rate={value}")

    @Slot()
    def update_rise_slew_rate(self):
        high_current=float(self.lineEdit_16.text())
        low_current=float(self.lineEdit.text())
        current_step=high_current-low_current
        value=float(self.lineEdit_9.text())
        slew_rate=round( (0.8*current_step/value)*1000 , 1 )
        self.lineEdit_6.setText(str(slew_rate))
        #self.push_msg_to_GUI(f"2 rise_time={value} slew_ret={slew_rate},")

    @Slot()
    def update_fall_time(self):
        high_current=float(self.lineEdit_16.text())
        low_current=float(self.lineEdit.text())
        current_step=high_current-low_current
        value=float(self.lineEdit_4.text())
        rise_time=round( (0.8*current_step/value)*1000 ,1 )
        self.lineEdit_10.setText(str(rise_time))
        #self.push_msg_to_GUI(f"1 rise_time={rise_time},slew_rate={value}")

    @Slot()
    def update_fall_slew_rate(self):
        high_current=float(self.lineEdit_16.text())
        low_current=float(self.lineEdit.text())
        current_step=high_current-low_current
        value=float(self.lineEdit_10.text())
        slew_rate=round( (0.8*current_step/value)*1000 , 1 )
        self.lineEdit_4.setText(str(slew_rate))
        #self.push_msg_to_GUI(f"2 rise_time={value} slew_ret={slew_rate},")

    def set_components_order(self):
        pass
    
    def set_window_title_with_debug_mode(self):
        if self.debug == True:
            self.setWindowTitle(self.Window_title+"_Debug mode")
            # Create a QPalette object
            palette = self.palette()
            
            # Set window background color to light blue
            palette.setColor(QPalette.Window, QColor(173, 216, 230))
            
            # Apply the modified palette to the window
            self.setPalette(palette)
        else:
            self.setWindowTitle(self.Window_title)

            # Create a QPalette object
            palette = self.palette()
            
            # Set window background color to light gray
            palette.setColor(QPalette.Window, QColor(240, 240, 240))
            
            # Apply the modified palette to the window
            self.setPalette(palette)


    def check_debug_mode(self):
        self.update_GUI()
        self.init_scope()
        #self.set_window_title_with_debug_mode()

        if self.lineEdit_7.text() == "53523962":
            self.set_debug_mode_enable(True)
            self.push_msg_to_GUI(f"debug is {self.debug}")
        else:
            self.set_debug_mode_enable(False)
        #self.pushButton_7.setEnabled(True)

    def set_debug_mode_enable(self):
        self.debug = not self.debug
        #self.set_window_title_with_debug_mode()
        self.push_msg_to_GUI(f"debug mode is {self.debug}")
        self.set_window_title_with_debug_mode()


    def init_scope(self):
        self.scope = myvisa.scope_types[self.parameter_setting_scope_resource_type](self.parameter_setting_scope_resource_address)

    def init_function_gen(self):
        self.function_gen = myvisa.function_gen_types[self.parameter_setting_function_gen_resource_type](self.parameter_setting_function_gen_resource_address)
 
    def update_GUI_then_save_waveform_once_time(self):
        the_filename=f"{self.lineEdit_7.text()}test"

        try:
            self.update_GUI_then_save_waveform(filename=the_filename)
        
            
            os.startfile(f"{self.lineEdit_27.text()}\\{the_filename}.png")
            QMessageBox.information(self, "Success", "Successfully saved on your PC")

        except:
            QMessageBox.about(self, "Warning", "can't save it on yoru PC")
    
    def update_GUI_then_save_waveform(self, filename="temp"):
        self.update_GUI()
        if self.comboBox.currentText() == "":
            QMessageBox.about(self, "Error", "Please check equipment setting on Settings page")
        else:
            self.save_waveform_in_scope_and_pc(filename)

    def save_waveform_in_scope_and_pc(self, filename="temp"):
        if self.debug == True:
            self.push_msg_to_GUI(f"save waveform as: {self.parameter_setting_scope_folder}/{filename}")
        if self.parameter_setting_screenshot_save_scope == True:
            scope_folder=self.parameter_setting_scope_folder
        else:
            scope_folder="none"
        if self.parameter_setting_screenshot_save_pc == True:
            local_folder=self.parameter_setting_local_folder
        else:
            local_folder="none"
        self.scope.save_waveform(scope_folder, filename, local_folder, self.debug)

    def set_scope_measurement_item(self, item_number=1, channel="1", item_type="max"):
        result = self.scope.set_measurement_items(item_number, channel, item_type)
        return result

    def get_scope_measurement_statistics(self, item_number=1, channel="1", item_type="max", item_statistic="mean"):
        result = self.scope.get_measurement_statistics(item_number, channel, item_type, item_statistic)
        return result

    def get_scope_measurement_value(self, item_number=1, channel="1", item_type="max"):
        result = self.scope.get_measurement_value(item_number, channel, item_type)
        return result

    def run_function_gen_3d_thread(self):
        # self.push_msg_to_GUI("run function gen 3d")
        self.update_GUI()
        if self.comboBox_2.currentText() == "" or self.comboBox.currentText() == "":
            QMessageBox.about(self, "Error", "Please check equipment setting on Settings page")
        else:
            self.function_gen_3d.start()
        # self.myprogpressbar.start()

    def stop_function_gen_3d_thread(self):
        self.function_gen_3d.stop()
        # self.push_msg_to_GUI("stop the 3d test")

    def set_progress_bar(self, data):
        self.progressBar.setValue(data)

    def open_3d_plot(self, filename="none", autosave=False):
        if filename == "none":
            self.get_filename(filetype="Excel Files (*.xls; *.xlsx)")
            filename = self.filenames[0]
        if self.debug == True:
            self.push_msg_to_GUI(f"opening 3D plot {filename}")
        vmax_spec,vmin_spec=self.open_dialog()
        pandas_report.plt_2d(filename,autosave,sheet_name="row",vmax_spec=vmax_spec,vmin_spec=vmin_spec)
        pandas_report.plt_3d(filename,autosave,sheet_name="row")

    def open_dialog(self):
        dialog = InputDialog(self)
        if dialog.exec():
            number1,number2 = dialog.get_input()
            #QMessageBox.information(self, "Input Received", f"You entered: {number1},{number2}")
        return number1,number2

    def update_GUI_then_send_to_function_gen_on(self):
        if self.comboBox_2.currentText() == "":
            QMessageBox.about(self, "Error", "Please select function generator on Settings page first")
        else:
            # only execute if on button is checked (otherwise, command will be sent twice)
            if self.radioButton.isChecked() == True:
                self.update_GUI_then_send_to_function_gen(function_output_enable=True)

    def update_GUI_then_send_to_function_gen_off(self):
        if self.comboBox_2.currentText() != "":
            # only execute if off button is checked (otherwise, command will be sent twice)
            if self.radioButton_2.isChecked() == True:
                self.update_GUI_then_send_to_function_gen(function_output_enable=False)

    def update_GUI_then_send_to_function_gen(self, function_output_enable):
        self.update_GUI()
        self.send_function_gen_command_one_time(self.parameter_main_frequency, self.parameter_main_duty, function_output_enable)

    def send_function_gen_command_one_time(self, freq, duty, on_off=False):
        if on_off == False:
            self.function_gen.off(self.parameter_setting_function_gen_channel)
        self.function_gen.set_load_impedance(self.parameter_main_load_impedance, self.parameter_setting_function_gen_channel)
        self.function_gen.set_waveform_shape("pulse", self.parameter_setting_function_gen_channel)
        self.function_gen.set_freq(freq, self.parameter_setting_function_gen_channel)
        self.function_gen.set_duty(duty, self.parameter_setting_function_gen_channel)
        high_voltage_value = float(self.parameter_main_high_current) * float(self.parameter_main_gain) / 1000
        low_voltage_value = float(self.parameter_main_low_current) * float(self.parameter_main_gain) / 1000
        self.function_gen.set_voltage_high(str(high_voltage_value), self.parameter_setting_function_gen_channel)
        self.function_gen.set_voltage_low(str(low_voltage_value), self.parameter_setting_function_gen_channel)
        self.function_gen.set_rise_time_ns(self.rise_time_nsec, self.parameter_setting_function_gen_channel)
        self.function_gen.set_fall_time_ns(self.fall_time_nsec, self.parameter_setting_function_gen_channel)
        if on_off == True:
            self.function_gen.on(self.parameter_setting_function_gen_channel)

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

    def auto_on_off_function_gen_when_parameters_changed(self):
        if self.radioButton_2.isChecked():
            self.update_GUI_then_send_to_function_gen_off()
            if self.debug:
                self.push_msg_to_GUI("update functon gen and turn it OFF")   
        else:
            self.update_GUI_then_send_to_function_gen_on()
            if self.debug:
                self.push_msg_to_GUI("update functon gen and turn it ON")
    def save_config(self):
        self.update_GUI()
        self.parameter_dict = {"GUI version":myappid,
                                "parameter_main_load_impedance": self.parameter_main_load_impedance,
                               "parameter_main_gain": self.parameter_main_gain,
                               "parameter_main_high_current": self.parameter_main_high_current,
                               "parameter_main_low_current": self.parameter_main_low_current,
                               "parameter_main_slew_rate_rise": self.parameter_main_slew_rate_rise,
                               "parameter_main_slew_rate_fall": self.parameter_main_slew_rate_fall,
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
                               "parameter_setting_scope_vout_channel": self.parameter_setting_scope_vout_channel,
                               "parameter_setting_scope_iout_channel": self.parameter_setting_scope_iout_channel,
                               "parameter_setting_function_gen_resource_type": self.parameter_setting_function_gen_resource_type,
                               "parameter_setting_function_gen_resource_address": self.parameter_setting_function_gen_resource_address,
                               "parameter_setting_function_gen_channel": self.parameter_setting_function_gen_channel,
                               "parameter_setting_scope_folder": self.parameter_setting_scope_folder,
                               "parameter_setting_local_folder": self.parameter_setting_local_folder,
                               "parameter_setting_filename": self.parameter_setting_filename,
                               "parameter_setting_screenshot_save_scope": self.parameter_setting_screenshot_save_scope,
                               "parameter_setting_screenshot_save_pc": self.parameter_setting_screenshot_save_pc,
                               "parameter_setting_filename_include_timestamp": self.parameter_setting_filename_include_timestamp,
                               "parameter_setting_autocreate_3d_plot": self.parameter_setting_autocreate_3d_plot,
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
            if dlg.exec():
                self.filenames = dlg.selectedFiles()
                if self.debug == True:
                    self.push_msg_to_GUI(self.filenames)

        except:
            QMessageBox.about(self, "Warning", "The file could not be opened")

    def load_config_from_filename(self, filenames):

        with open(filenames[0], 'r') as j:
            json_data = json.load(j)
            if self.debug == True:
                self.push_msg_to_GUI(str(json_data))

            self.comboBox_8.setCurrentText(json_data["parameter_main_load_impedance"])
            self.lineEdit_17.setText(str(json_data["parameter_main_gain"]))
            self.lineEdit_16.setText(str(json_data["parameter_main_high_current"]))
            self.lineEdit.setText(str(json_data["parameter_main_low_current"]))
            self.lineEdit_6.setText(str(json_data["parameter_main_slew_rate_rise"]))
            self.lineEdit_4.setText(str(json_data["parameter_main_slew_rate_fall"]))
            self.lineEdit_5.setText(str(json_data["parameter_main_duty"]))
            self.lineEdit_8.setText(str(json_data["parameter_main_frequency"]))
            # =============================
            self.lineEdit_13.setText(str(json_data["parameter_main_duty_list"])[1:-1])
            self.lineEdit_15.setText(str(json_data["parameter_main_freq_list"])[1:-1])
            self.lineEdit_21.setText(str(json_data["parameter_main_ton_duration_time_sec"]))
            self.lineEdit_22.setText(str(json_data["parameter_main_toff_duration_time_sec"]))
            self.checkBox_3.setChecked(json_data["parameter_main_roll_up_down_enable"])
            # ==================================
            self.comboBox_6.setCurrentText(json_data["parameter_setting_scope_resource_type"])
            self.comboBox.setCurrentText(json_data["parameter_setting_scope_resource_address"])
            self.comboBox_3.setCurrentText(json_data["parameter_setting_scope_vout_channel"])
            self.comboBox_4.setCurrentText(json_data["parameter_setting_scope_iout_channel"])
            self.comboBox_7.setCurrentText(json_data["parameter_setting_function_gen_resource_type"])
            self.comboBox_2.setCurrentText(json_data["parameter_setting_function_gen_resource_address"])
            self.comboBox_5.setCurrentText(json_data["parameter_setting_function_gen_channel"])
            self.lineEdit_26.setText(json_data["parameter_setting_scope_folder"])
            self.lineEdit_27.setText(json_data["parameter_setting_local_folder"])
            self.lineEdit_7.setText(str(json_data["parameter_setting_filename"]))
            self.checkBox_4.setChecked(json_data["parameter_setting_screenshot_save_scope"])
            self.checkBox_5.setChecked(json_data["parameter_setting_screenshot_save_pc"])
            self.checkBox_2.setChecked(json_data["parameter_setting_filename_include_timestamp"])
            self.checkBox_6.setChecked(json_data["parameter_setting_autocreate_3d_plot"])
        self.update_GUI()
            
    def update_GUI(self):
        # get GUI import
        # main page
        self.parameter_main_load_impedance = self.comboBox_8.currentText()
        self.parameter_main_gain = float(self.lineEdit_17.text())
        self.parameter_main_high_current = float(self.lineEdit_16.text())
        self.parameter_main_low_current = float(self.lineEdit.text())
        self.parameter_main_slew_rate_rise = float(self.lineEdit_6.text())
        self.parameter_main_slew_rate_fall = float(self.lineEdit_4.text())
        self.parameter_main_duty = float(self.lineEdit_5.text())
        self.parameter_main_frequency = float(self.lineEdit_8.text())
        self.update_rise_and_fall_time()

        # ======
        self.parameter_main_duty_list = eval("["+str(self.lineEdit_13.text())+"]")
        self.parameter_main_freq_list = eval("["+str(self.lineEdit_15.text())+"]")
        self.parameter_main_ton_duration_time_sec = float(self.lineEdit_21.text())
        self.parameter_main_toff_duration_time_sec = float(self.lineEdit_22.text())
        self.parameter_main_roll_up_down_enable = self.checkBox_3.isChecked()

        # setting page
        self.parameter_setting_scope_resource_type = self.comboBox_6.currentText()
        self.parameter_setting_scope_resource_address = self.comboBox.currentText()
        self.parameter_setting_scope_vout_channel = self.comboBox_3.currentText()
        self.parameter_setting_scope_iout_channel = self.comboBox_4.currentText()
        self.parameter_setting_function_gen_resource_type = self.comboBox_7.currentText()
        self.parameter_setting_function_gen_resource_address = self.comboBox_2.currentText()
        self.parameter_setting_function_gen_channel = self.comboBox_5.currentText()
        self.parameter_setting_scope_folder = self.lineEdit_26.text()
        self.parameter_setting_local_folder = self.lineEdit_27.text()
        self.parameter_setting_filename = self.lineEdit_7.text()
        self.parameter_setting_screenshot_save_scope = self.checkBox_4.isChecked()
        self.parameter_setting_screenshot_save_pc = self.checkBox_5.isChecked()
        self.parameter_setting_filename_include_timestamp = self.checkBox_2.isChecked()
        self.parameter_setting_autocreate_3d_plot = self.checkBox_6.isChecked()
         
    def update_scope_address(self):
        if self.comboBox.currentText() != "":
            try:
                self.update_GUI()
                self.init_scope()
                self.lineEdit_28.setText(self.scope.get_equipment_name())
                info = self.scope.info()
                if info != 0:
                    self.push_msg_to_GUI(info)
            except:
                QMessageBox.about(self, "Error", "Connection to scope not successful")
                self.comboBox.setCurrentIndex(0)
                self.lineEdit_28.setText("")

    def update_function_gen_address(self):
        if self.comboBox_2.currentText() != "":
            try:
                self.update_GUI()
                self.init_function_gen()
                self.lineEdit_29.setText(self.function_gen.get_equipment_name())
                info = self.function_gen.info()
                if info != 0:
                    self.push_msg_to_GUI(info)
            except:
                QMessageBox.about(self, "Error", "Connection to function generator not successful")
                self.comboBox_2.setCurrentIndex(0)
                self.lineEdit_29.setText("")

    def set_horizontal_scale_in_scope(self, scale_value="1e-6"):
        self.scope.set_horizontal_scale(scale_value)

    def update_rise_and_fall_time(self):
        if self.parameter_main_high_current < self.parameter_main_low_current:
            QMessageBox.about(self, "Error", "Low current needs to be set <= High current!")
            self.lineEdit.setText(self.lineEdit_16.text())
            self.parameter_main_high_current = float(self.lineEdit_16.text())
            self.parameter_main_low_current = float(self.lineEdit.text())
            return None
        if self.parameter_main_slew_rate_rise <= 0:
            QMessageBox.about(self, "Error", "Slew rate (rise) may not be <= 0!")
            self.lineEdit_6.setText("50.0")
            self.parameter_main_slew_rate_rise = float(self.lineEdit_6.text())
            return None        
        if self.parameter_main_slew_rate_fall <= 0:
            QMessageBox.about(self, "Error", "Slew rate (fall) may not be <= 0!")
            self.lineEdit_4.setText("50.0")
            self.parameter_main_slew_rate_fall = float(self.lineEdit_4.text())
            return None
        self.update_rise_time()
        self.update_fall_time()
        self.update_rise_slew_rate()
        self.update_fall_slew_rate()
        
        self.rise_time_nsec=float(self.lineEdit_9.text())
        self.fall_time_nsec=float(self.lineEdit_10.text())
        #self.label_26.setText(f"Rise time: {self.rise_time_nsec} ns")
        #self.fall_time_nsec=round( (self.parameter_main_high_current - self.parameter_main_low_current) / self.parameter_main_slew_rate_fall *1000)
        #self.label_27.setText(f"Fall time: {self.fall_time_nsec} ns")
        
    
    def clear_message_box(self):
        self.textEdit.clear()

    def select_directory(self):
        self.dir_path = QFileDialog.getExistingDirectory(
            self, "Chose Directory", "./")
        self.lineEdit_27.setText(self.dir_path)

    def about_the_gui(self):
        QMessageBox.about(self, "About the GUI", 'Powered by PySide6, <a href=https://github.com/a9202507/ifx_gui_for_core_power_validation>Github</a>')

    def update_frequency_list_on_gui(self):
        startfreq=int(self.lineEdit_11.text())
        endfreq=int(self.lineEdit_12.text())
        stepfreq=int(self.lineEdit_14.text())
        frequency_list=[]
        for freq in range(startfreq,endfreq+1,stepfreq):
            frequency_list.append(freq)
        string_list = [str(element) for element in frequency_list]
        delimiter = ", "
        result_string = delimiter.join(string_list)
        
        
        self.lineEdit_15.setText(result_string)

    # short key for operation     
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Q:
            self.radioButton_2.setChecked(True)
        elif event.key() == Qt.Key_Space:
            self.radioButton.setChecked(True)
        else:
            super().keyPressEvent(event)

class InputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Input spec for 2D curve")
        
        self.layout = QVBoxLayout()
        validator = QDoubleValidator(0, 2.5, 3)
        validator.setNotation(QDoubleValidator.StandardNotation)
        self.line_edit = QLineEdit(self)
        self.line_edit.setValidator(validator)
        self.line_edit.setPlaceholderText("Enter a number for Vmax spec")
        self.layout.addWidget(self.line_edit)

        self.line_edit_2 = QLineEdit(self)
        self.line_edit_2.setValidator(validator)
        self.line_edit_2.setPlaceholderText("Enter a number for Vmin spec")
        self.layout.addWidget(self.line_edit_2)
        
        self.button = QPushButton("Submit", self)
        self.button.clicked.connect(self.handle_submit)
        self.layout.addWidget(self.button)
        
        self.setLayout(self.layout)
    
    def handle_submit(self):
        input_text = float(self.line_edit.text())
        if isinstance(input_text,float):
            self.accept()
        else:
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid number.")
    
    def get_input(self):
        return self.line_edit.text(),self.line_edit_2.text()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWin = MyMainWindow(debug=False)

    myWin.show()

    sys.exit(app.exec())
