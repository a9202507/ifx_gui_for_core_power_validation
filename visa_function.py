import pyvisa
import time
import pathlib
from datetime import datetime
rm = pyvisa.ResourceManager()


def get_visa_resource_list(remove_ASRL_devices=False):
    rm = pyvisa.ResourceManager()
    device_list = rm.list_resources()

    if remove_ASRL_devices == True:
        filtered = filter(lambda device: "ASRL" not in device, device_list)
        device_list = list(filtered)
    else:
        pass

    return device_list


class visa_equipment():
    def __init__(self, visa_resource_name):
        self.visa_resource_name = visa_resource_name
        self.inst = pyvisa.ResourceManager().open_resource(self.visa_resource_name)
    '''
    def write(self, visa_str=""):
        self.inst.write(visa_str)

    def query(self, visa_str=""):
        self.inst.query(visa_str)
    '''

    def get_equipment_name(self):
        self.equipment_name = self.inst.query("*IDN?")
        return self.equipment_name


class tek_visa_equipment(visa_equipment):
    def __init__(self, visa_resource_name):
        visa_equipment.__init__(self, visa_resource_name)

    def on(self):
        self.inst.write("OUTPut1:STATe ON")

    def off(self):
        self.inst.write("OUTPut1:STATe off")



class Tektronix_AFG3000(tek_visa_equipment):
    def __init__(self, visa_resource_name, shape="PULS"):
        tek_visa_equipment.__init__(self, visa_resource_name)
        self.set_waveform_shape(shape)

    def set_freq(self, freq_khz):
        self.inst.write("SOURce1:FREQuency:FIXed "+str(freq_khz)+"kHz")

    def set_duty(self, duty):
        self.inst.write("SOURce1:PULSe:DCYCLe "+str(duty))

    def set_rise_time_ns(self, rise_time):
        self.inst.write("SOURce1:PULSe:TRANsition:LEADing " +
                        str(rise_time)+"ns")

    def set_fall_time_ns(self, fall_time):
        self.inst.write("SOURce1:PULSe:TRANsition:TRAiling " +
                        str(fall_time)+"ns")

    def set_waveform_shape(self, shape="PULS"):
        self.inst.write("SOURce1:FUNCtion:SHAPe "+shape)

    def set_voltage_high(self, voltage=0):
        self.inst.write("SOURce1:VOLTage:LEVel:IMMediate:High "+str(voltage))

    def set_voltage_low(self, voltage=0):
        self.inst.write("SOURce1:VOLTage:LEVel:IMMediate:Low "+str(voltage))

    def get_rise_time_ns(self):
        return self.inst.query("SOURce1:PULSe:TRANsition:LEADing?")
    
    def set_output_impedance(self,impedance_value='INFinity'):
        self.inst.write(f"OUTPut1:IMPedance {impedance_value}")



class Tektronix_MSO4x_MSO5x_MSO6x(visa_equipment):
    def __init__(self, visa_resource_name):
        visa_equipment.__init__(self, visa_resource_name)

    def save_waveform_in_inst(self, scope_folder, filename="temp.png", debug=False):
        command_code=f"SAVE:IMAGe '{scope_folder}/{filename}'"
        self.inst.write(command_code)
        if debug == True:
            print(command_code)

    def read_file_in_inst(self, scope_folder, filename):
        self.inst.write(f"FILESystem:READFile '{scope_folder}/{filename}'")

    def save_waveform_back_to_pc(self, scope_folder, filename, local_directory="./report", debug=False):
        if debug == True:
            print(f"save waveform: {scope_folder}/{filename}")
        self.inst.write(f"FileSystem:READFile '{scope_folder}/{filename}'")
        imgData = self.inst.read_raw(1024*1024)
        file = open(f"{local_directory}/{filename}", "wb")
        file.write(imgData)
        file.close()

        ## work
    def set_waveform_directory_in_scope(self, directory="E:/20220530"):
        self.inst.write(f"FILESystem:CWD '{directory}'")

        ## work
    def get_waveform_directory_in_scope(self):
        directory = self.inst.query(f"FILESystem:CWD?")
        return directory

        ##work
    def set_measurement_items(self, item_number='1', channel_number='1', measure_item_type="mean"):

        self.inst.write("MEASUrement:MEAS"+str(item_number) +
                        ":SOURCE CH"+channel_number)

        
        self.inst.write("MEASUrement:MEAS"+str(item_number) +
                        ":TYPE "+measure_item_type)


        ## can't work on 2024/01/17
    def get_measurement_value(self, item_number="1", measure_item_type="mean"):
        measure_type_dict = {"max": "MAXimum",
                             "min": "MINimum",
                             "mean": "MEAN",
                             "value": "value", }

        result = self.inst.query(
            "MEASUrement:MEAS"+str(item_number)+":RESUlts:CURRentacq:"+measure_type_dict[measure_item_type]+"?")

        return result

    def set_horizontal_scale(self, scale="2e-6"): ## work
        self.inst.write("HORIZONTAL:SCAlE "+scale)

    def set_trigger_level(self, trigger_level="1.0"): ## work
        self.inst.write("TRIGger:A:level "+trigger_level)

    def set_trigger_channel(self, channel="CH1"): ##work
        self.inst.write(f"TRIGger:A:EDGE:SOURCE {channel}")



class Tektronix_MSO5000_DPO5000_DP07000(visa_equipment):
    def __init__(self, visa_resource_name):
        visa_equipment.__init__(self, visa_resource_name)

    def set_measurement_items(self, item_number='1', channel_number='1', measure_item_type="mean"):

        self.inst.write(f"MEASUrement:MEAS{item_number}:TYPE {measure_item_type}") 
        self.inst.write(f"MEASUrement:MEAS{item_number}:SOURCE1 CH{channel_number}")               
        self.inst.write(f"MEASUrement:MEAS{item_number}:STATE ON")

    def get_measurement_value(self, item_number="1", measure_item_type="mean"):
        measure_type_dict = {"max": "MAXimum",
                             "min": "MINimum",
                             "mean": "MEAN",
                             "value": "value", }

        result = self.inst.query(f"MEASUrement:MEAS{item_number}:VALue?")
        return result
    '''
    dpo7054c command example
    MEASUrement:MEAS1:TYPE pk2pk -> set N1 measure type to peak-to-peak
    MEASUrement:MEAS1:TYPE max   -> set N1 measure type to max
    MEASUrement:MEAS1:TYPE mini  -> set N1 measure type to mini
    MEASUrement:MEAS1:TYPE rms   -> set N1 measure type to rms
    MEASUrement:MEAS1:TYPE mean  -> set N1 measure type to mean
    '''

    def save_waveform_in_inst(self, scope_folder, filename="temp.png", debug=False):
        self.inst.write("HARDCopy:PORT FILE;")
        self.inst.write("EXPort:FORMat PNG")
        command_code=f"HARDCopy:FILEName '{scope_folder}/{filename}'"
        self.inst.write(command_code)
        self.inst.write("HARDCopy STARt")
        if debug == True:
            print(command_code)

    def read_file_in_inst(self, scope_folder, filename):
        self.inst.write(f"FILESystem:READFile '{scope_folder}/{filename}'")
    
    def save_waveform_back_to_pc(self, scope_folder, filename, local_directory="./report", debug=False):
        if debug == True:
            print(f"save waveform: {scope_folder}/{filename}")
        self.inst.write(f"FileSystem:READFile '{scope_folder}/{filename}'")
        imgData = self.inst.read_raw(1024*1024)
        file = open(f"{local_directory}/{filename}", "wb")
        file.write(imgData)
        file.close()

    def set_waveform_directory_in_scope(self, directory="C:/TekScope/Screenshots"):
        self.inst.write(f"FILESystem:CWD '{directory}'")
        
    def get_waveform_directory_in_scope(self):
        directory = self.inst.query(f"FILESystem:CWD?")
        return directory

    def set_horizontal_scale(self, scale="2e-6"):
        self.inst.write("HORIZONTAL:SCAlE "+scale)

    def set_trigger_level(self, trigger_level="1.0"):
        self.inst.write("TRIGger:A:level "+trigger_level)

    def set_trigger_channel(self, channel="CH1"):
        self.inst.write(f"TRIGger:A:EDGE:SOURCE {channel}")



'''
def save_waveform_in_inst(visaRsrcAddr, fileSaveLocationInInst, filename, timestamp_enable=True, debug=False):
    rm = pyvisa.ResourceManager()
    scope = rm.open_resource(visaRsrcAddr)
    visaRsrcAddr = visaRsrcAddr
    fileSaveLocation2 = pathlib.Path(fileSaveLocationInInst)
    dt = datetime.now()
    timestamp = dt.strftime("MSO56_%Y%m%d_%H%M%S.png")
    if timestamp_enable == True:
        filename_in_inst = filename+timestamp
    else:
        filename_in_inst = filename

    rm = pyvisa.ResourceManager()
    scope = rm.open_resource(visaRsrcAddr)

    path_filename_in_inst = "'"+str(fileSaveLocation2 / filename_in_inst)+"'"
    scope.write('SAVE:IMAGe '+path_filename_in_inst)
    if debug == True:

        print(scope.query('*IDN?'))  # Print instrument id to console window

        print('SAVE:IMAGe '+path_filename_in_inst)
    scope.close()
    rm.close()
'''

if __name__ == '__main__':

    devices = get_visa_resource_list()
    print(devices)
    scope=tek_visa_dpo_escope(devices[1])
    
    
