import pyvisa as visa
rm = visa.ResourceManager()
print(rm.list_resources())
escope=visa.ResourceManager().open_resource("USB0::0x0699::0x0522::C040569::INSTR")
path=r'C:\temp'
filename=r'\test_local_1858.png'
escope.write(f"SAVE:IMAGe \'{path+filename}\'")
escope.baud_rate=57600

local_path_filename=r'C:\Users\Echen3\Desktop\Temp\test_local_20220113_1015.png'

#escope.write('FILESystem:READFile '+path+filename)
scope.write('FILESystem:READFile '+local_path_filename)
imgData = escope.read_raw(1)
file = open(local_path_filename, 'wb')
file.write(imgData)
file.close()
