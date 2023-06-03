# LoadSlammer_GUI
Users can use this GUI to control Tektronix scope and function generator equipments to do 3D transinet validation. 

Designed by Pyside2 and Python3.6.5

# equipment list

Tektronix MSO66b Windows10 base escope
Tektronix function generator AFG3021C

# software requirment

Windows 10 64bits 
Python 3.6.5 32bits
Pyside2 for UI
GPIB driver, check with your GPIB cable vendor if you have to use GIPB cable.

# before start-up
1. coonected your equipment to your notebook, GPIB/USB/Ethernet all are acceptable.
2. install realted libraies from requirements.txt

# start-up
1. run main.py 
2. goes to setting page, press "rescan" buttom on GUI to scans your equipment
3. select your escope and function generator on setting page.
4. goes to main page and select your transient conditions.
5. press "run 3D" buttom" to start your validation.    
