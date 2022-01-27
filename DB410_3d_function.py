import visa_function as myvisa
import time
def DB410_3d_function(fungen_resource_name,
                      scope_resource_name,
                      folder_name_in_inst,
                      file_name,
                      high_voltage_v,
                      low_voltage_v,
                      freq_khz_list,
                      duty_list,
                      rise_time_ns,
                      fall_time_ns,
                      delay_time_sec,
                      cool_down_time_sec,
                      file_name_with_timestamp=True,
                      debug=False,
                      ):
    fun_gen=myvisa.tek_visa_functionGen(fungen_resource_name)
    scope=myvisa.tek_visa_mso_escope(scope_resource_name)
    fun_gen.set_voltage_high(high_voltage_v)
    fun_gen.set_voltage_low(low_voltage_v)
    if debug == True:
        print(f"3d function.py: high current={high_voltage_v}, low current={low_voltage_v}")
    
    for freq in freq_khz_list:
        for duty in duty_list:
            fun_gen.on()
            fun_gen.set_freq(freq)
            fun_gen.set_duty(duty)
            fun_gen.set_rise_time_ns(rise_time_ns)
            fun_gen.set_fall_time_ns(fall_time_ns)
            time.sleep(delay_time_sec)
            scope.save_waveform_in_inst(folder_name_in_inst,file_name+str(freq)+"Khz"+"_D"+str(duty),file_name_with_timestamp,debug)
            time.sleep(delay_time_sec)
            fun_gen.off()
            time.sleep(cool_down_time_sec)
            

            if debug == True:
                print(f"freq {freq},duty{duty}")

    fun_gen.off()


if __name__ == "__main__":

    devices=myvisa.get_visa_resource_list()
    print(devices)
    DB410_3d_function(devices[4],
                      devices[0],
                      "C:/Users/Tek_Local_Admin/Desktop/Eason",
                      "Eason_function",
                      0.38,                    
                      0.28,
                      [10,20,100,200],
                      [10,20,30,40,50],
                      760,
                      760,
                      2,
                      cool_down_time_sec=5,
                      file_name_with_timestamp=True,
                      debug=True,
                      )
            
            
    
