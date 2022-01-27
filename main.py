# Rev2022.1.27 for beta release
# a9202507@gmail.com

import sys
from PySide2.QtCore import QThread
from PySide2.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
import PySide2_DB410_ui
import json
import os
import visa_function as myvisa
import pandas as pd
import DB410_3d_function


class DB410_3d_thread(QThread):
    #vr3d_to_enable_abort = pyqtSignal(bool)
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        pass
        myWin.update_GUI()
        DB410_3d_function.DB410_3d_function(fungen_resource_name=myWin.parameter_setting_function_gen_resource_name,
                                            scope_resource_name=myWin.parameter_setting_scope_resource_name ,
                                            folder_name_in_inst=myWin.parameter_setting_folder_in_inst,
                                            file_name=myWin.parameter_setting_filename+str(myWin.parameter_main_high_current)+"A_"+str(myWin.parameter_main_low_current)+"A_"+f"Gain{myWin.parameter_main_gain}mVA_",
                                            high_voltage_v=myWin.parameter_main_high_current * myWin.parameter_main_gain / 1000,
                                            low_voltage_v=myWin.parameter_main_low_current* myWin.parameter_main_gain/1000,
                                            freq_khz_list=myWin.parameter_main_freq_list,
                                            duty_list=myWin.parameter_main_duty_list,
                                            rise_time_ns=myWin.parameter_main_rise_fall_nsec,
                                            fall_time_ns=myWin.parameter_main_rise_fall_nsec,
                                            delay_time_sec=myWin.parameter_main_delay_time_sec,
                                            cool_down_time_sec=myWin.parameter_main_cooldown_time_sec,
                                            file_name_with_timestamp=myWin.parameter_setting_filename_include_timestamp,
                                            debug=myWin.debug,
                                            )    
        
        


    def stop(self):
        self.terminate()

    def stop(self):
        self.terminate()

class MyMainWindow(QMainWindow, PySide2_DB410_ui.Ui_MainWindow):
    def __init__(self, parent=None,debug=False):
        super(MyMainWindow, self).__init__(parent)
        self.setFixedSize(516, 900)
        self.setupUi(self)

        # set windowTitle
        self.setWindowTitle("DB410 Rev.2022.01.27")
        
        #self.pushButton_8.clicked.connect(self.create_visa_equipment)
        self.pushButton_8.clicked.connect(self.run_function_gen_3d_thread)
        self.pushButton_4.clicked.connect(self.stop_function_gen_3d_thread)
        self.pushButton_6.clicked.connect(self.update_equipment_on_combox)
        self.pushButton_2.clicked.connect(self.send_function_gen_command_one_time)
        self.actionLoad_config.triggered.connect(self.load_config)
        self.actionSave_config.triggered.connect(self.save_config)
        self.actionAbout_the_GUI.triggered.connect(self.about_the_GUI)
        self.about_the_gui_text="powered by PySide2 and Python3."
        self.debug=debug

        ## start-up function
        self.update_equipment_on_combox()
        
        ## set auto load init.json during startup
        self.path=os.path.dirname(os.path.abspath(__file__))
        self.path_file_list=list()
        self.path_file_list.append(self.path+"\init.json")
        self.load_config_from_filename(self.path_file_list)

        ## initial thread
        self.function_gen_3d = DB410_3d_thread()
        
        if self.debug==True:
            self.push_msg_to_GUI("==debugging mode==")

    def run_function_gen_3d_thread(self):
        self.push_msg_to_GUI("run function gen 3d")
        self.update_GUI()
        self.function_gen_3d.start()
        #self.myprogpressbar.start()
    def stop_function_gen_3d_thread(self):
        self.function_gen_3d.stop()
        self.push_msg_to_GUI("stop the 3d test")

    def send_function_gen_command_one_time(self):
        function_gen=myvisa.tek_visa_functionGen(self.comboBox_2.currentText())
        function_gen.set_duty(self.lineEdit_5.text())
        function_gen.set_freq(self.lineEdit_8.text())

        high_voltage_value=float(self.lineEdit_16.text())*float(self.lineEdit_17.text())/1000
        low_voltage_value=float(self.lineEdit.text())*float(self.lineEdit_17.text())/1000
        function_gen.set_voltage_high(str(high_voltage_value))        
        function_gen.set_voltage_low(str(low_voltage_value))
        function_gen.set_rise_time_ns(self.lineEdit_6.text())
        function_gen.set_fall_time_ns(self.lineEdit_4.text())

        if self.comboBox_3.currentText() == "on":
            function_gen.on()
        else:
            function_gen.off()

    def create_visa_equipment(self):
        if self.comboBox.currentText() != "":
            
            self.escope=myvisa.create_visa_equipment(self.comboBox.currentText())
            message=self.escope.query('*IDN?')
            if self.debug==True:
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
        self.resource_list=myvisa.get_visa_resource_list()
        if self.debug==True:
            self.push_msg_to_GUI(self.resource_list)
        
    def push_msg_to_GUI(self,msg=""):
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
                                   "parameter_main_duty_list":self.parameter_main_duty_list,
                                   "parameter_main_slew_nsec": self.parameter_main_slew_nsec,
                                   "parameter_main_freq_list": self.parameter_main_freq_list,
                                   "parameter_main_delay_time_sec": self.parameter_main_delay_time_sec,
                                   "roll_up_down_enable": self.roll_up_down_enable,
                               }
        filename_with_path = QFileDialog.getSaveFileName(
            self, 'Save File', '.', 'JSON Files (*.json)')
        save_filename = filename_with_path[0]
        if save_filename != "":
            with open(save_filename, 'w') as fp:
                #json.dump(self.parameter_dict, fp)
                fp.write(json.dumps(self.parameter_dict, indent=4))
                                   
        if self.debug==True:
            self.push_msg_to_GUI(self.parameter_dict)

    
    def load_config(self):

        self.get_filename()
        print(self.filenames[0])
        self.load_config_from_filename(self.filenames)

    def get_filename(self):
        try:
            dlg = QFileDialog(self, 'Open File', '.','JSON Files (*.json);;All Files (*)')
            if dlg.exec_():
                self.filenames = dlg.selectedFiles()
                if self.debug==True:
                    self.push_msg_to_GUI(self.filenames)
                   
        except:
            QMessageBox.about(self,"Warning","the filename isn't work")

    def load_config_from_filename(self,filenames):
        
        with open(filenames[0], 'r') as j:
            json_data = json.load(j)
            if self.debug==True:
                self.push_msg_to_GUI(str(json_data))
            self.lineEdit_18.setText(json_data["parameter_main_high_current"])
            self.lineEdit_3.setText(json_data["parameter_main_low_current"])
            self.lineEdit_12.setText(json_data["parameter_main_gain"])
            self.lineEdit_13.setText(str(json_data["parameter_main_duty_list"])[1:-1])
            self.lineEdit_14.setText(json_data["parameter_main_slew_nsec"])
            self.lineEdit_15.setText(str(json_data["parameter_main_freq_list"])[1:-1])
            self.lineEdit_21.setText(json_data["parameter_main_delay_time_sec"])
            self.checkBox_3.setChecked(json_data["roll_up_down_enable"])
        
            
    def about_the_GUI(self):
        QMessageBox.about(self, "about the GUI", self.about_the_gui_text)


    def update_GUI(self):
        # get GUI import
        # main page
        self.parameter_main_high_current=float(self.lineEdit_18.text())
        self.parameter_main_low_current=float(self.lineEdit_3.text())
        self.parameter_main_gain=float(self.lineEdit_12.text())
        self.parameter_main_duty_list = eval("["+str(self.lineEdit_13.text())+"]")
        self.parameter_main_rise_fall_nsec=float(self.lineEdit_14.text())
        self.parameter_main_freq_list = eval("["+str(self.lineEdit_15.text())+"]")
        self.parameter_main_delay_time_sec=float(self.lineEdit_21.text())
        self.parameter_main_cooldown_time_sec=float(self.lineEdit_22.text())        
        self.roll_up_down_enable = self.checkBox_3.isChecked()

        # setting page
        self.parameter_setting_function_gen_resource_name=self.comboBox_2.currentText()
        self.parameter_setting_scope_resource_name=self.comboBox.currentText()
        self.parameter_setting_folder_in_inst=self.lineEdit_26.text()
        self.parameter_setting_filename=self.lineEdit_7.text()
        self.parameter_setting_filename_include_timestamp=self.checkBox_2.isChecked()
        self.parameter_setting_ffilename_include_transient=self.checkBox.isChecked()

        
if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWin = MyMainWindow(debug=True)

    myWin.show()

    sys.exit(app.exec_())
