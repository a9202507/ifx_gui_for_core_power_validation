from gpib_class import *
import time

'''
fungen=gpibTekFunctionGen(15)
fungen.set_waveform_shape()
fungen.on()
'''
####
tek_mso56_ip_addr="192.168.0.187"
tek_mso56_resource="TCPIP0::192.168.0.187::inst0::INSTR"
###

'''
for i in range(1,100):
    fungen.set_freq(i)
    for j in range(0,51,10):
        fungen.set_duty(j)
        time.sleep(2)
'''
        

#fungen.off()
rm=visa.ResourceManager()
scope=rm.open_resource(tek_mso56_resource)
scope.write('SAVE:IMAGe \'C:\\Temp\Temp4.png\'')


scope.write('FILESystem:READFile \'C:\\Temp\Temp4.png\'')

imgData = scope.read_raw()

# Save image data to local disk
filename=r'C:\Users\Echen3\Desktop\Temp\test_local_1.png'
file = open(filename, 'wb')
file.write(imgData)
file.close()
