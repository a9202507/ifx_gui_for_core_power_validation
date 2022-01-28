# Rev2022.1.27 for beta release
# a9202507@gmail.com

from socket import MsgFlag
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


class DB410_3d_thread(QThread):
    DB410_msg = Signal(str)
    DB410_process_bar = Signal(int)

    def __init__(self):
        QThread.__init__(self)
        #self.DB410_msg = Signal(str)

    def __del__(self):
        self.wait()

    def run(self):
        self.DB410_msg.emit("==run 3D test==")
        myWin.update_GUI()

        '''
        if myWin.debug == True:
            print(
                f"type myWin.parameter_main_high_current={myWin.parameter_main_high_current}")
        DB410_3d_function.DB410_3d_function(fungen_resource_name=myWin.parameter_setting_function_gen_resource_name,
                                            scope_resource_name=myWin.parameter_setting_scope_resource_name,
                                            folder_name_in_inst=myWin.parameter_setting_folder_in_inst,
                                            file_name=myWin.parameter_setting_filename+str(myWin.parameter_main_high_current)+"A_"+str(
                                                myWin.parameter_main_low_current)+"A_"+f"Gain{myWin.parameter_main_gain}mVA_",
                                            high_voltage_v=myWin.parameter_main_high_current *
                                            myWin.parameter_main_gain / 1000,
                                            low_voltage_v=myWin.parameter_main_low_current * myWin.parameter_main_gain/1000,
                                            freq_khz_list=myWin.parameter_main_freq_list,
                                            duty_list=myWin.parameter_main_duty_list,
                                            rise_time_ns=myWin.parameter_main_rise_fall_time_nsec,
                                            fall_time_ns=myWin.parameter_main_rise_fall_time_nsec,
                                            delay_time_sec=myWin.parameter_main_delay_time_sec,
                                            cool_down_time_sec=myWin.parameter_main_cooldown_time_sec,
                                            file_name_with_timestamp=myWin.parameter_setting_filename_include_timestamp,
                                            debug=myWin.debug,
                                            )
                                            '''
        freq_list_len = len(myWin.parameter_main_freq_list)
        duty_list_len = len(myWin.parameter_main_duty_list)

        for freq_idx, freq in enumerate(myWin.parameter_main_freq_list):
            for duty_idx, duty in enumerate(myWin.parameter_main_duty_list):

                self.DB410_msg.emit(f"Freq={str(freq)}, Duty={str(duty)}")
                self.DB410_process_bar.emit(
                    int((duty_idx+freq_idx*duty_list_len)/(freq_list_len*duty_list_len)*100))
                myWin.run_function_gen(
                    myWin.parameter_setting_function_gen_resource_name, True)

                time.sleep(myWin.parameter_main_delay_time_sec)
                myWin.run_function_gen(
                    myWin.parameter_setting_function_gen_resource_name, False)
        self.DB410_process_bar.emit(100)
        '''
        for i in range(1, 100):
            self.DB410_msg.emit(str(i))

            self.DB410_process_bar.emit(int(i/3))
            time.sleep(0.1)
        '''
        self.DB410_msg.emit("==3D test finish==")

    def stop(self):
        self.DB410_msg.emit("==3D test stop==")
        self.DB410_process_bar.emit(0)
        # todo
        self.terminate()


class MyMainWindow(QMainWindow, PySide2_DB410_ui.Ui_MainWindow):
    def __init__(self, parent=None, debug=False):
        super(MyMainWindow, self).__init__(parent)
        self.setFixedSize(516, 900)
        self.setupUi(self)

        # set windowTitle
        self.setWindowTitle("DB410 Rev.2022.01.28 Beta")

        # self.pushButton_8.clicked.connect(self.create_visa_equipment)
        self.pushButton_8.clicked.connect(self.run_function_gen_3d_thread)
        self.pushButton_4.clicked.connect(self.stop_function_gen_3d_thread)
        self.pushButton_6.clicked.connect(self.update_equipment_on_combox)
        self.pushButton_2.clicked.connect(
            self.send_function_gen_command_one_time)
        self.actionLoad_config.triggered.connect(self.load_config)
        self.actionSave_config.triggered.connect(self.save_config)
        self.actionAbout_the_GUI.triggered.connect(self.about_the_GUI)
        self.about_the_gui_text = "powered by PySide2 and Python3."
        self.debug = debug

        # start-up function
        self.update_equipment_on_combox()

        # set auto load init.json during startup
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.path_file_list = list()
        self.path_file_list.append(self.path+"\init.json")
        self.load_config_from_filename(self.path_file_list)

        # initial thread
        self.function_gen_3d = DB410_3d_thread()
        self.function_gen_3d.DB410_msg.connect(self.push_msg_to_GUI)
        self.function_gen_3d.DB410_process_bar.connect(self.set_process_bar)

        if self.debug == True:
            self.push_msg_to_GUI("==debugging mode==")

    def set_process_bar(self, data):
        self.progressBar.setValue(data)

    def run_function_gen_3d_thread(self):
        #self.push_msg_to_GUI("run function gen 3d")
        self.update_GUI()
        self.function_gen_3d.start()
        # self.myprogpressbar.start()

    def stop_function_gen_3d_thread(self):
        self.function_gen_3d.stop()
        #self.push_msg_to_GUI("stop the 3d test")

    def run_function_gen(self, function_gen_resource_name, on_off):
        self.function_gen = myvisa.tek_visa_functionGen(
            self.comboBox_2.currentText())

        if on_off == True:
            self.function_gen.on()
        else:
            self.function_gen.off()

    def send_function_gen_command_one_time(self):
        self.function_gen = myvisa.tek_visa_functionGen(
            self.comboBox_2.currentText())
        self.function_gen.set_duty(self.lineEdit_5.text())
        self.function_gen.set_freq(self.lineEdit_8.text())

        high_voltage_value = float(
            self.lineEdit_16.text())*float(self.lineEdit_17.text())/1000
        low_voltage_value = float(self.lineEdit.text()) * \
            float(self.lineEdit_17.text())/1000
        self.function_gen.set_voltage_high(str(high_voltage_value))
        self.function_gen.set_voltage_low(str(low_voltage_value))
        self.function_gen.set_rise_time_ns(self.lineEdit_6.text())
        self.function_gen.set_fall_time_ns(self.lineEdit_4.text())

        if self.comboBox_3.currentText() == "on":
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
        self.comboBox_2.clear()
        self.comboBox.addItem("")
        self.comboBox.addItems(self.resource_list)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItems(self.resource_list)

    def get_visa_resource(self):
        self.resource_list = myvisa.get_visa_resource_list()
        if self.debug == True:
            self.push_msg_to_GUI(self.resource_list)

    def push_msg_to_GUI(self, msg=""):
        if True:
            self.textEdit.append(str(msg))
            self.textEdit.append("")
        else:
            pass

    def save_config(self):
        self.update_GUI()
        self.parameter_dict = {"parameter_main_high_current": self.parameter_main_high_current,
                               "parameter_main_low_current": self.parameter_main_low_current,
                               "parameter_main_gain": self.parameter_main_gain,
                               "parameter_main_duty_list": self.parameter_main_duty_list,
                               "parameter_main_rise_fall_time_nsec": self.parameter_main_rise_fall_time_nsec,
                               "parameter_main_freq_list": self.parameter_main_freq_list,
                               "parameter_main_delay_time_sec": self.parameter_main_delay_time_sec,
                               "parameter_main_roll_up_down_enable": self.parameter_main_roll_up_down_enable,
                               "parameter_main_cooldown_time_sec": self.parameter_main_cooldown_time_sec,
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
        print(self.filenames[0])
        self.load_config_from_filename(self.filenames)

    def get_filename(self):
        try:
            dlg = QFileDialog(self, 'Open File', '.',
                              'JSON Files (*.json);;All Files (*)')
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
            self.lineEdit_18.setText(
                str(json_data["parameter_main_high_current"]))
            self.lineEdit_3.setText(
                str(json_data["parameter_main_low_current"]))
            self.lineEdit_12.setText(str(json_data["parameter_main_gain"]))
            self.lineEdit_13.setText(
                str(json_data["parameter_main_duty_list"])[1:-1])
            self.lineEdit_14.setText(str(
                json_data["parameter_main_rise_fall_time_nsec"]))
            self.lineEdit_15.setText(
                str(json_data["parameter_main_freq_list"])[1:-1])
            self.lineEdit_21.setText(str(
                json_data["parameter_main_delay_time_sec"]))
            self.checkBox_3.setChecked(
                json_data["parameter_main_roll_up_down_enable"])
            self.lineEdit_22.setText(str(
                json_data["parameter_main_cooldown_time_sec"]))
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
        self.parameter_main_high_current = float(self.lineEdit_18.text())
        self.parameter_main_low_current = float(self.lineEdit_3.text())
        self.parameter_main_gain = float(self.lineEdit_12.text())
        self.parameter_main_duty_list = eval(
            "["+str(self.lineEdit_13.text())+"]")
        self.parameter_main_rise_fall_time_nsec = float(
            self.lineEdit_14.text())
        self.parameter_main_freq_list = eval(
            "["+str(self.lineEdit_15.text())+"]")
        self.parameter_main_delay_time_sec = float(self.lineEdit_21.text())
        self.parameter_main_cooldown_time_sec = float(self.lineEdit_22.text())
        self.parameter_main_roll_up_down_enable = self.checkBox_3.isChecked()

        # setting page
        self.parameter_setting_function_gen_resource_name = self.comboBox_2.currentText()
        self.parameter_setting_scope_resource_name = self.comboBox.currentText()
        self.parameter_setting_folder_in_inst = self.lineEdit_26.text()
        self.parameter_setting_filename = self.lineEdit_7.text()
        self.parameter_setting_filename_include_timestamp = self.checkBox_2.isChecked()
        self.parameter_setting_filename_include_transient = self.checkBox.isChecked()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWin = MyMainWindow(debug=True)

    myWin.show()

    sys.exit(app.exec_())
