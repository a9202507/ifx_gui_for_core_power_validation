#-------------------------------------------------------------------------------
# Name:  Save Screenshot (Hard Copy) to PC for 5 Series MSO Oscilloscopes
#
# Purpose:  This example demonstrates how to save a screen shot (hard copy) image
#  from a 5 Series MSO oscilloscope to the PC.
#
# Development Environment: Python 3.6, PyVisa 1.8, NI-VISA 2017, Windows 10 x64
#
# Compatible Instruments: 5 Series MSO, MSO54, MSO56, MSO58
#
# Compatible Interfaces:  USB, Ethernet
#
# Tektronix provides the following example "AS IS" with no support or warranty.
#
#-------------------------------------------------------------------------------

from datetime import datetime # std library
import time # std library
import pyvisa as visa # https://pyvisa.readthedocs.io/

from io import BytesIO
#import win32clipboard
from PIL import Image
import pathlib

# Replace string with your instrument's VISA Resource Address
visaRsrcAddr = "USB0::0x0699::0x0522::C040569::INSTR"
fileSaveLocation = r'C:\Temp\\' # Folder on your PC where to save image
fileSaveLocation2 = pathlib.Path("C:/Temp")
filename_in_inst='Temp_pathlib_test.png'
rm = visa.ResourceManager()
scope = rm.open_resource(visaRsrcAddr)
print(scope.query('*IDN?'))  # Print instrument id to console window

# Save image to instrument's local disk
#scope.write('SAVE:IMAGe \'C:\\Temp\Temp.png\'')
#scope.write('SAVE:IMAGe \'C:\\Temp\Temp2.png\'')
#scope.write('SAVE:IMAGe \'C:\\Temp\Temp3.png\'')


print('SAVE:IMAGe \'C:\\Temp\Temp.png\'')
path_filename_in_inst="'"+str(fileSaveLocation2 / filename_in_inst)+"'"
scope.write('SAVE:IMAGe '+path_filename_in_inst)
print('SAVE:IMAGe '+path_filename_in_inst)

# Generate a filename based on the current Date & Time
dt = datetime.now()
fileName = dt.strftime("MSO5_%Y%m%d_%H%M%S.png")

# Wait for instrument to finish writing image to disk
scope.query('*OPC?')

# Read image file from instrument
scope.write('FILESystem:READFile \'C:\\Temp\Temp.png\'')
print("my")
imgData = scope.read_raw()

# Save image data to local disk
file = open(fileSaveLocation + fileName, "wb")
file.write(imgData)
file.close()

# Copy image to clipboard

def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()

filepath = fileSaveLocation + fileName
image = Image.open(filepath)

output = BytesIO()
image.convert("RGB").save(output, "BMP")
data = output.getvalue()[14:]
output.close()

#send_to_clipboard(win32clipboard.CF_DIB, data)
print('Copy image to clipboard')

# Image data has been transferred to PC and saved. Delete image file from instrument's hard disk.
#scope.write('FILESystem:DELEte \'C:\\Temp\Temp.png\'')

scope.close()
rm.close()
