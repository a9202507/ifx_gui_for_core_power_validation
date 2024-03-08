# Infineon GUI for core power validation

Users can use this GUI to control a scope and a function generator to do 3D transient validation.

Designed with Pyside6 and Python 3.12.2/64bits, (32bits isn't workable due to PySide6 library requirements)

# Equipment list

### Scopes
- Tektronix MSO4x / MSO5x / MSO6x (Win10 based)
- Tektronix MSO5000 / DPO5000 / DPO7000 (Win7 based)
- Siglent SDS1000X-E / SDS2000X-E
### Function generators
- Tektronix AFG3000
- Siglent SDG1000X / SDG2000X / SDG6000X
- Keysight 332x0A (WARNING: this instrument has limitations in rise / fall time settings)

# Software requirements

Windows 10 64bits
Python 3.12.2 64bits
Pyside6 for UI
GPIB driver, check with your GPIB cable vendor if you have to use GIPB cable.

# Before start-up

1. Connect your equipment to your PC, GPIB/USB/Ethernet are all acceptable.
2. Install libraries from requirements.txt.

# Start-up

1. Run main.py.
2. Go to Settings page, press "re-scan equipment" button on GUI to scan your equipment, if not already listed.
3. Select your scope and function generator on Settings page.
4. Go to main page and select your transient conditions.
5. Press "Start 3D test" button" to start your validation.
