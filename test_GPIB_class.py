import gpib_class


escope=gpib_class.usbMsoEscope()
#escope=gpib_class.ipv4MsoEscope("192.168.0.187")
path=r'C:\temp'
			    
filename=r'\test_local_1854.png'
			    
escope.save_file_escope(path,filename)


local_filename=r'C:\Users\Echen3\Desktop\Temp\test_local_21.png'
escope.save_file_to_local(path,filename,local_filename)



