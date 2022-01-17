import visa_function as myvisa
import time
def DB410_3d_function(resource_name,
                      high_voltage_mv,
                      low_voltage_mv,
                      freq_khz_list,
                      duty_list,
                      rise_time_ns,
                      fall_time_ns,
                      delay_time_sec,
                      debug=False,
                      ):
    fun_gen=myvisa.tek_visa_functionGen(resource_name)
    fun_gen.set_voltage_high(high_voltage_mv)
    fun_gen.set_voltage_low(low_voltage_mv)
    fun_gen.set_rise_time_ns(rise_time_ns)
    fun_gen.set_fall_time_ns(fall_time_ns)
    fun_gen.on()
    for freq in freq_khz_list:
        for duty in duty_list:
            time.sleep(delay_time_sec)

            if debug == True:
                print(f"freq {freq},duty{duty}")

    fun_gen.off()


if __name__ == "__main__":

    print(myvisa.get_visa_resource_list())
    DB410_3d_function('USB0::0x0699::0x0522::C040569::INSTR',
                      0.2,
                      0.05,
                      [10,20,100,200],
                      [10,20,30,40,50],
                      1976,
                      1976,
                      2,
                      debug=True
                      )
            
            
    
