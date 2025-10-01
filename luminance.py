from colorcal import ColorCAL
# %%
import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
for port in ports:
    print(f"port: {port.device}")
    print(f"description: {port.description}")
    print(f"hwid: {port.hwid}")
    print("---")

# %%

cc = ColorCAL(port='/dev/cu.usbmodem00001')

# %% 

if cc.getNeedsCalibrateZero():
    print("Zero calibration needed!")
    print("Please cover the sensor completely (make it totally dark)")
    input("Press Enter when sensor is covered...")
    
    success = cc.calibrateZero()
    if success:
        print("Zero calibration successful!")
    else:
        print("Calibration failed - make sure sensor is completely covered")
else:
    print("Zero calibration not needed - already calibrated at factory")
# %%
# check if connected
if cc.ok:
    print("connected successfully!")
    print(f"serial: {cc.serialNum}")
    print(f"firmware: {cc.firm}")
    
    # check if zero calibration needed
    if cc.getNeedsCalibrateZero():
        print("cover the sensor and calibrate...")
        # cc.calibratezero()
    
    # take a measurement
    ok, x, y, z = cc.measure()
    if ok:
        print(f"luminance: {y} cd/m²")
else:
    print("connection failed")

# %% 
