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



class Tektronix_AFG3000(visa_equipment):
    def __init__(self, visa_resource_name):
        visa_equipment.__init__(self, visa_resource_name)

    waveform_shape_dict = {"pulse": "PULSe",
                           "sine": "SINusoid",
                           "square": "SQUare",
                           "dc": "DC"}

    def on(self, channel="1"):
        self.inst.write(f"OUTPut{channel}:STATe ON")

    def off(self, channel="1"):
        self.inst.write(f"OUTPut{channel}:STATe off")

    def set_freq(self, freq_khz, channel="1"):
        self.inst.write(f"SOURce{channel}:FREQuency:FIXed {freq_khz}kHz")

    def set_duty(self, duty, channel="1"):
        self.inst.write(f"SOURce{channel}:PULSe:DCYCLe {duty}")

    def set_rise_time_ns(self, rise_time, channel="1"):
        self.inst.write(f"SOURce{channel}:PULSe:TRANsition:LEADing {rise_time}ns")

    def set_fall_time_ns(self, fall_time, channel="1"):
        self.inst.write(f"SOURce{channel}:PULSe:TRANsition:TRAiling {fall_time}ns")

    def set_waveform_shape(self, shape="pulse", channel="1"):
        self.inst.write(f"SOURce{channel}:FUNCtion:SHAPe {self.waveform_shape_dict[shape]}")

    def set_voltage_high(self, voltage=0, channel="1"):
        self.inst.write(f"SOURce{channel}:VOLTage:LEVel:IMMediate:High {voltage}")

    def set_voltage_low(self, voltage=0, channel="1"):
        self.inst.write(f"SOURce{channel}:VOLTage:LEVel:IMMediate:Low {voltage}")

    def get_rise_time_ns(self, channel="1"):
        return self.inst.query(f"SOURce{channel}:PULSe:TRANsition:LEADing?")
    
    def set_output_impedance(self,impedance_value="HiZ", channel="1"):
        if impedance_value=="HiZ":
            self.inst.write(f"OUTPut{channel}:IMPedance INFinity")
        else:
            self.inst.write(f"OUTPut{channel}:IMPedance {impedance_value}")

    def info(self):
        return 0



class Siglent_SDG1000X_SDG2000X_SDG6000X(visa_equipment):
    def __init__(self, visa_resource_name):
        visa_equipment.__init__(self, visa_resource_name)

    waveform_shape_dict = {"pulse": "PULSE",
                           "sine": "SINE",
                           "square": "SQUARE",
                           "dc": "DC"}

    def on(self, channel="1"):
        self.inst.write(f"C{channel}:OUTPut ON")

    def off(self, channel="1"):
        self.inst.write(f"C{channel}:OUTPut OFF")

    def set_freq(self, freq_khz, channel="1"):
        self.inst.write(f"C{channel}:BaSic_WaVe FRQ,{float(freq_khz)*1000}")

    def set_duty(self, duty, channel="1"):
        self.inst.write(f"C{channel}:BaSic_WaVe DUTY,{duty}")

    def set_rise_time_ns(self, rise_time, channel="1"):
        self.inst.write(f"C{channel}:BaSic_WaVe RISE,{float(rise_time)/1000000000}")

    def set_fall_time_ns(self, fall_time, channel="1"):
        self.inst.write(f"C{channel}:BaSic_WaVe FALL,{float(fall_time)/1000000000}")

    def set_waveform_shape(self, shape="pulse", channel="1"):
        self.inst.write(f"C{channel}:BaSic_WaVe WVTP,{self.waveform_shape_dict[shape]}")

    def set_voltage_high(self, voltage=0, channel="1"):
        self.inst.write(f"C{channel}:BaSic_WaVe HLEV,{voltage}")

    def set_voltage_low(self, voltage=0, channel="1"):
        self.inst.write(f"C{channel}:BaSic_WaVe LLEV,{voltage}")

    def get_rise_time_ns(self):
        # This would return the complete waveform settings, needs to be parsed for the rise time. Not used, therefore not yet implemented.
        #return self.inst.query(f"C{channel}:BaSic_WaVe?")
        pass

    def set_output_impedance(self, impedance_value="HiZ", channel="1"):
        if impedance_value=="HiZ":
            self.inst.write(f"C{channel}:OUTPut LOAD,HZ")
        else:
            self.inst.write(f"C{channel}:OUTPut LOAD,{impedance_value}")

    def info(self):
        return 0



class Keysight_332x0A(visa_equipment):
    def __init__(self, visa_resource_name):
        visa_equipment.__init__(self, visa_resource_name)

    waveform_shape_dict = {"pulse": "PULSe",
                           "sine": "SINusoid",
                           "square": "SQUare",
                           "dc": "DC"}

    def on(self, channel="1"):
        self.inst.write(f"OUTPut:STATe ON")

    def off(self, channel="1"):
        self.inst.write(f"OUTPut:STATe off")

    def set_freq(self, freq_khz, channel="1"):
        self.inst.write(f"SOURce:FREQuency {freq_khz}kHz")

    def set_duty(self, duty, channel="1"):
        self.inst.write(f"SOURce:FUNCtion:PULSe:DCYCLe {duty}")

    def set_rise_time_ns(self, rise_time, channel="1"):
        self.inst.write(f"SOURce:FUNCtion:PULSe:TRANsition {rise_time}ns")

    def set_fall_time_ns(self, fall_time, channel="1"):
        # rise time and fall time will be the same for this function generator
        pass

    def set_waveform_shape(self, shape="pulse", channel="1"):
        self.inst.write(f"SOURce:FUNCtion {self.waveform_shape_dict[shape]}")

    def set_voltage_high(self, voltage=0, channel="1"):
        self.inst.write(f"SOURce:VOLTage:HIGH {voltage}")

    def set_voltage_low(self, voltage=0, channel="1"):
        self.inst.write(f"SOURce:VOLTage:LOW {voltage}")

    def get_rise_time_ns(self, channel="1"):
        return self.inst.query(f"SOURce:PULSe:TRANsition?")

    def set_output_impedance(self,impedance_value="HiZ", channel="1"):
        if impedance_value=="HiZ":
            self.inst.write(f"OUTPut:LOAD INFinity")
        else:
            self.inst.write(f"OUTPut:LOAD {impedance_value}")

    def info(self):
        return "WARNING Keysight_332x0A:\n- Rise time value is used for both rise and fall time\n- Supported range for rise/fall time:\n   20ns - 100ns (33210A)\n   5ns - 100ns (33220A)"



class Tektronix_MSO4x_MSO5x_MSO6x(visa_equipment):
    def __init__(self, visa_resource_name):
        visa_equipment.__init__(self, visa_resource_name)

    measure_type_dict = {"max": "MAXimum",
                         "min": "MINimum",
                         "pkpk": "PK2PK",
                         "mean": "MEAN",
                         "rms": "RMS",
                         "frequency": "FREQuency",
                         "period": "PERIod",
                         "duty": "PDUty",
                         "nduty": "NDUty"}
    measure_stat_dict = {"max": "MAXimum",
                         "min": "MINimum",
                         "mean": "MEAN",
                         "value": "MEAN", #not supported? take mean instead... 
                         "count": "POPUlation"}

        ##work
    def set_measurement_items(self, item_number=1, channel="1", item_type="max"):
        self.inst.write("MEASUrement:MEAS"+str(item_number)+":SOURCE CH"+channel)
        self.inst.write("MEASUrement:MEAS"+str(item_number)+":TYPE "+self.measure_type_dict[item_type])


        ## can't work on 2024/01/17
    def get_measurement_value(self, item_number=1, channel="1", item_type="max"):
        result = self.inst.query("MEASUrement:MEAS"+str(item_number)+":RESUlts:CURRentacq:"+self.measure_stat_dict[item_statistic]+"?")
        return result

    def get_measurement_statistics(self, item_number=1, channel="1", item_type="max", item_statistic="mean"):
        result = self.inst.query("MEASUrement:MEAS"+str(item_number)+":RESUlts:CURRentacq:"+self.measure_stat_dict[item_statistic]+"?")
        return result
        
    def reset_statistics(self):
        # not supported? probably not needed, setting the horizontal scale probably also resets statistics...
        pass

    def save_waveform(self, scope_folder, filename="temp", local_folder="./report", debug=False):
        if scope_folder != "none":
            # save in scope_folder
            command_code=f"SAVE:IMAGe '{scope_folder}/{filename}.png'"
            self.inst.write(command_code)
            if debug == True:
                print(command_code)
            #time.sleep(1)
        if local_folder != "none":
            if debug == True:
                print(f"save waveform: {local_folder}/{filename}.png")
            if scope_folder != "none":
                # copy file which was already saved in scope_folder to PC
                self.inst.write(f"FileSystem:READFile '{scope_folder}/{filename}.png'")
                imgData = self.inst.read_raw(1024*1024)
                file = open(f"{local_folder}/{filename}.png", "wb")
                file.write(imgData)
                file.close()
            else:
                # save in temp file in scope and copy to PC
                self.inst.write(f"SAVE:IMAGe 'C:/temp.png'")
                #time.sleep(1)
                self.inst.write(f"FileSystem:READFile 'C:/temp.png'")
                imgData = self.inst.read_raw(1024*1024)
                file = open(f"{local_folder}/{filename}.png", "wb")
                file.write(imgData)
                file.close()
                self.inst.write(f"FileSystem:READFile 'C:/temp.png'")

    def read_file_in_inst(self, scope_folder, filename):
        self.inst.write(f"FILESystem:READFile '{scope_folder}/{filename}'")


        ## work
    def set_waveform_directory_in_scope(self, directory="E:/20220530"):
        self.inst.write(f"FILESystem:CWD '{directory}'")

        ## work
    def get_waveform_directory_in_scope(self):
        directory = self.inst.query(f"FILESystem:CWD?")
        return directory

    def acq_run(self):
        self.inst.write("TRIGger:A:MODe AUTO")
        self.inst.write("ACQuire:STATE RUN")

    def acq_stop(self):
        self.inst.write("ACQuire:STATE STOP")

    def set_horizontal_scale(self, scale="2e-6"): ## work
        self.inst.write("HORIZONTAL:SCAlE "+scale)

    def set_trigger(self, channel="1", level="1.0", coupling="DC"):
        self.inst.write(f"TRIGger:A:EDGE:SOUrce CH{channel}")
        self.inst.write(f"TRIGger:A:EDGE:COUPling {coupling}")
        self.inst.write("TRIGger:A:EDGE:SLOPE RISe")
        if level == "auto":
            self.inst.write("TRIGger:A SETLevel")
        else:
            self.inst.write(f"TRIGger:A:LEVel:CH{channel} {level}")

    def info(self):
        return 0



class Tektronix_MSO5000_DPO5000_DPO7000(visa_equipment):
    def __init__(self, visa_resource_name):
        visa_equipment.__init__(self, visa_resource_name)

    measure_type_dict = {"max": "MAXimum",
                         "min": "MINImum",
                         "pkpk": "PK2PK",
                         "mean": "MEAN",
                         "rms": "RMS",
                         "frequency": "FREQuency",
                         "period": "PERIod",
                         "duty": "PDUty",
                         "nduty": "NDUty"}
    measure_stat_dict = {"max": "MAXimum",
                         "min": "MINImum",
                         "mean": "MEAN",
                         "value": "VALue", 
                         "count": "COUNt"}

    def set_measurement_items(self, item_number=1, channel="1", item_type="max"):
        self.inst.write(f"MEASUrement:MEAS{item_number}:TYPE {self.measure_type_dict[item_type]}") 
        self.inst.write(f"MEASUrement:MEAS{item_number}:SOURCE1 CH{channel}")               
        self.inst.write(f"MEASUrement:MEAS{item_number}:STATE ON")
        self.inst.write("MEASUrement:STATIstics:MODe ALL")
    '''
    dpo7054c command example
    MEASUrement:MEAS1:TYPE pk2pk -> set N1 measure type to peak-to-peak
    MEASUrement:MEAS1:TYPE max   -> set N1 measure type to max
    MEASUrement:MEAS1:TYPE mini  -> set N1 measure type to mini
    MEASUrement:MEAS1:TYPE rms   -> set N1 measure type to rms
    MEASUrement:MEAS1:TYPE mean  -> set N1 measure type to mean
    '''

    def get_measurement_value(self, item_number=1, channel="1", item_type="max"):
        result = self.inst.query(f"MEASUrement:MEAS{item_number}:VALue?")
        return result

    def get_measurement_statistics(self, item_number=1, channel="1", item_type="max", item_statistic="mean"):
        result = self.inst.query(f"MEASUrement:MEAS{item_number}:{self.measure_stat_dict[item_statistic]}?")
        return result

    def reset_statistics(self):
        self.inst.write("MEASUrement:STATIstics:COUNt RESET")

    def save_waveform(self, scope_folder, filename="temp", local_folder="./report", debug=False):
        self.inst.write("HARDCopy:PORT FILE;")
        self.inst.write("EXPort:FORMat PNG")
        if scope_folder != "none":
            # save in scope_folder
            command_code=f"HARDCopy:FILEName '{scope_folder}/{filename}.png'"
            self.inst.write(command_code)
            self.inst.write("HARDCopy STARt")
            if debug == True:
                print(command_code)
            #time.sleep(1)
        if local_folder != "none":
            if debug == True:
                print(f"save waveform: {local_folder}/{filename}.png")
            if scope_folder != "none":
                # copy file which was already saved in scope_folder to PC
                self.inst.write(f"FileSystem:READFile '{scope_folder}/{filename}.png'")
                imgData = self.inst.read_raw(1024*1024)
                file = open(f"{local_folder}/{filename}.png", "wb")
                file.write(imgData)
                file.close()
            else:
                # save in temp file in scope and copy to PC
                self.inst.write(f"HARDCopy:FILEName 'C:/temp.png'")
                self.inst.write("HARDCopy STARt")
                #time.sleep(1)
                self.inst.write(f"FileSystem:READFile 'C:/temp.png'")
                imgData = self.inst.read_raw(1024*1024)
                file = open(f"{local_folder}/{filename}.png", "wb")
                file.write(imgData)
                file.close()
                self.inst.write(f"FileSystem:DELEte 'C:/temp.png'")

    def read_file_in_inst(self, scope_folder, filename):
        self.inst.write(f"FILESystem:READFile '{scope_folder}/{filename}'")
    
    def set_waveform_directory_in_scope(self, directory="C:/TekScope/Screenshots"):
        self.inst.write(f"FILESystem:CWD '{directory}'")
        
    def get_waveform_directory_in_scope(self):
        directory = self.inst.query(f"FILESystem:CWD?")
        return directory

    def acq_run(self):
        self.inst.write("TRIGger:A:MODe AUTO")
        self.inst.write("ACQuire:STATE RUN")

    def acq_stop(self):
        self.inst.write("ACQuire:STATE STOP")

    def set_horizontal_scale(self, scale="2e-6"):
        self.inst.write("HORIZONTAL:SCAlE "+scale)

    def set_trigger(self, channel="1", level="1.0", coupling="DC"):
        self.inst.write(f"TRIGger:A:EDGE:SOURCE CH{channel}")
        self.inst.write(f"TRIGger:A:EDGE:COUPling {coupling}")
        self.inst.write("TRIGger:A:EDGE:SLOPE RISe")
        if level == "auto":
            self.inst.write("TRIGger:A SETLevel")
        else:
            self.inst.write(f"TRIGger:A:LEVel:CH{channel} {level}")

    def info(self):
        return 0



class Siglent_SDS1000XE_SDS2000XE(visa_equipment):
    def __init__(self, visa_resource_name):
        visa_equipment.__init__(self, visa_resource_name)

    measure_type_dict = {"max": "MAX",
                         "min": "MIN",
                         "pkpk": "PKPK",
                         "mean": "MEAN",
                         "rms": "RMS",
                         "frequency": "FREQ",
                         "period": "PER",
                         "duty": "DUTY",
                         "nduty": "NDUTY"}
    measure_stat_dict = {"max": "max",
                         "min": "min",
                         "mean": "mean",
                         "value": "cur", 
                         "count": "count"}

    def set_measurement_items(self, item_number=1, channel="1", item_type="max"):
        # only five custom measurements are supported
        if item_number < 6:
            self.inst.write(f"PARAMETER_CUSTOM {self.measure_type_dict[item_type]},C{channel}") 
            self.inst.write("PASTAT ON")

    def get_measurement_value(self, item_number=1, channel="1", item_type="max"):
        reply = self.inst.query(f"C{channel}:PARAMETER_VALUE? {self.measure_type_dict[item_type]}")
        result = reply.split(",")[1] # split to get the value
        result = result.replace("V", "") #remove the unit V
        result = result.replace("A", "") #remove the unit A
        return result

    def get_measurement_statistics(self, item_number=1, channel="1", item_type="max", item_statistic="mean"):
        # only five custom measurements with statistics are supported. If statistics are off or item_number>6, current value could be queried (not yet implemented).
        if item_number < 6:
            reply = self.inst.query(f"PARAMETER_VALUE? STAT{item_number}")
            reply = reply.replace("\n", "")
            resultlist = reply.split(":")[1].split(",") # split to get list in format (cur, XXX, mean, XXX, min, XXX, max, XXX, std-dev, XXX, count, XXX)
            if resultlist[0] == "OFF": # measurement not enabled correctly
                result="invalid"
            else:
                result = resultlist[resultlist.index(self.measure_stat_dict[item_statistic])+1] # look for the relevant statistic value in the list
                result = result.replace("V", "") #remove the unit
                result = result.replace("A", "") #remove the unit
        else:
            result="invalid"
        if result == "invalid": # try to get current measurement from channel
            result = self.get_measurement_value(item_number, channel, item_type)
        return result

    def reset_statistics(self):
        self.inst.write("PASTAT RESET")

    def save_waveform(self, scope_folder, filename="temp", local_folder="./report", debug=False):
        # only saving to PC in BMP format supported
        if scope_folder == "none":
            # don't save in scope
            pass
        else:
            # not supported anyway
            pass
        if local_folder == "none":
            # don't save on PC
            pass
        else:
            self.inst.write("SCDP")
            #time.sleep(1)
            imgData = self.inst.read_raw()
            file = open(f"{local_folder}/{filename}.bmp", "wb")
            file.write(imgData)
            file.close()
            if debug == True:
                print(f"save waveform: {local_folder}/{filename}.bmp")

    def read_file_in_inst(self, scope_folder, filename):
        # not supported
        pass

    def set_waveform_directory_in_scope(self, directory="C:/TekScope/Screenshots"):
        # not supported
        pass
        
    def get_waveform_directory_in_scope(self):
        # not supported
        directory = ""
        return directory

    def acq_run(self):
        self.inst.write("TRIG_MODE AUTO") # setting trigger to auto also starts acquisition

    def acq_stop(self):
        self.inst.write("STOP")

    def set_horizontal_scale(self, scale="2e-6"):
        self.inst.write(f"TIME_DIV {scale}")

    def set_trigger(self, channel="1", level="1.0", coupling="DC"):
        self.inst.write(f"C{channel}:TRIG_COUPLING {coupling}")
        self.inst.write(f"C{channel}:TRIG_SLOPE POS")
        if level == "auto":
            self.inst.write("SET50")
        else:
            self.inst.write(f"C{channel}:TRIG_LEVEL {level}")

    def info(self):
        return "INFO Siglent SDS1000X-E / SDS2000X-E:\nSaving screenshots on scope is not supported"



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



# define scope and function generator types as dictionaries, pointing to the visa class.
scope_types = {        "Tektronix MSO4x / MSO5x / MSO6x": Tektronix_MSO4x_MSO5x_MSO6x,
                       "Tektronix MSO5000 / DPO5000 / DPO7000": Tektronix_MSO5000_DPO5000_DPO7000,
                       "Siglent SDS1000X-E / SDS2000X-E": Siglent_SDS1000XE_SDS2000XE}
function_gen_types = { "Tektronix AFG3000": Tektronix_AFG3000,
                       "Siglent SDG1000X / SDG2000X / SDG6000X": Siglent_SDG1000X_SDG2000X_SDG6000X,
                       "Keysight 332x0A": Keysight_332x0A}



if __name__ == '__main__':

    devices = get_visa_resource_list()
    print(devices)
    
