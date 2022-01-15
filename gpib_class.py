## 2019/11/13 , eason.chen@infineon.com
## 2022/1/11    adding tek mso escope function

import visa                                                     # import GPIB module
import time
import datetime
import os
import pandas as pd


def scanGPIB():
    rm = visa.ResourceManager()
    res = rm.list_resources()
    gpib_list=list()
    gpib_device_name=list()
    gpib_temp_dict={}
    results_pd=pd.DataFrame()
    for device in range(1,(len(res))):                              #len(res) -> find device Q'ty , res[-1] is latest device , 
        inst=rm.open_resource(res[device])
        gpib_list.append(res[device])
        gpib_device_name.append(inst.query('*IDN?'))
        gpib_temp_dict['Addr']=res[device][7:-7]
        iqn_temp=inst.query('*IDN?')        
        gpib_temp_dict['Vendor']=iqn_temp[:(iqn_temp.find(","))]
        ## find first ","
        char_s=iqn_temp.find(",")
        ## find 2nd ","
        char_e=iqn_temp.find(",",(char_s)+1)
        ## cut string between 1st(",") to 2nd(",)
        gpib_temp_dict['Model']=iqn_temp[char_s+1:char_e]
        gpib_temp_dict['other']=iqn_temp[char_e+1:]
                
        ## create dataframe
        results_pd=results_pd.append(gpib_temp_dict,ignore_index=True)
    return results_pd

class gpibMachine():
    def __init__(self,GPIBaddr):
        self.gpibaddr=GPIBaddr
        self.rm=visa.ResourceManager()
        self.device=visa.ResourceManager().open_resource('GPIB0::'+str(GPIBaddr)+'::INSTR')
        IDN=self.device.query('*IDN?')
        self.vendor=IDN[:(IDN.find(","))]
        char_s=IDN.find(",")    # find 1st ","
        char_e=IDN.find(",",(char_s)+1) #find 2nd ","
        self.model=IDN[char_s+1:char_e]
        
class gpibTekMachine(gpibMachine):
    def __init__(self,GPIBaddr):
        gpibMachine.__init__(self,GPIBaddr)
    def on(self):
        self.device.write("OUTPut1:STATe ON")
    def off(self):
        self.device.write("OUTPut1:STATe OFF")

class gpibTekFunctionGen(gpibTekMachine):
    def __init__(self,GPIBaddr,shape="PULS"):
        gpibTekMachine.__init__(self,GPIBaddr)
        self.set_waveform_shape(shape)
    def set_freq(self,freq_khz):
        self.device.write("SOURce1:FREQuency:FIXed "+str(freq_khz)+"kHz")
    def set_duty(self,duty):
        self.device.write("SOURce1:PULSe:DCYCLe "+str(duty))
    def set_rise_time_ns(self,rise_time):
        self.device.write("SOURce1:PULSe:TRANsition:LEADing "+str(rise_time)+"ns")
    def set_fall_time_ns(self,fall_time):
        self.device.write("SOURce1:PULSe:TRANsition:TRAiling "+str(fall_time)+"ns")
    def set_waveform_shape(self,shape="PULS"):
        self.device.write("SOURce1:FUNCtion:SHAPe "+shape)
    def set_voltage_high(self,voltage=0):
        self.device.write("SOURce1:VOLTage:LEVel:IMMediate:High "+str(voltage))
    def set_voltage_low(self,voltage=0):
        self.device.write("SOURce1:VOLTage:LEVel:IMMediate:Low "+str(voltage))

    def get_rise_time_ns(self):
        return self.device.query("SOURce1:PULSe:TRANsition:LEADing?")

    
class usbMsoEscope():
    def __init__(self):
        self.rm=visa.ResourceManager()
        self.device=visa.ResourceManager().open_resource("USB0::0x0699::0x0522::C040569::INSTR")
    def save_file_escope(self,path,filename):
        self.device.write(f"SAVE:IMAGe \'{path+filename}\'")
    def save_file_to_local(self,path,filename,local_path_filename):
        self.write('FILESystem:READFile '+path+filename)
        imgData = self.read_raw()
        file = open(local_path_filename, 'wb')
        file.write(imgData)
        file.close()
'''    
class ipv4MsoEscope():
    def __init__(self,ipv4_address):
        self.rm=visa.ResourceManager()
        self.device=visa.ResourceManager().open_resource("TCPIP0::"+ipv4_address+"::inst0::INSTR")
    def save_file_escope(self,path,filename):
        self.device.write(f"SAVE:IMAGe \'{path+filename}\'")
    def save_file_to_local(self,path,filename,local_path_filename):
        self.write('FILESystem:READFile '+path,filename,local_path_filename)
        imgData = scope.read_raw()
        file = open(local_path_filename, 'wb')
        file.write(imgData)
        file.close()


    def read_ch_vmax(self,channel):
        pass
    def read_ch_vmin(self,channel):
        pass
'''
if __name__ == "__main__":
    #tek15=gpibTekFunctionGen(15)
    #tek15.set_freq(12)
    #tek15.set_duty(10)
    pass
