from colorcal import ColorCAL
# %%
import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
for port in ports:
    print(f"Port: {port.device}")
    print(f"Description: {port.description}")
    print(f"HWID: {port.hwid}")
    print("---")

# %%

cc = ColorCAL(port='/dev/cu.usbmodem00001')
# %%
# Check if connected
if cc.OK:
    print("Connected successfully!")
    print(f"Serial: {cc.serialNum}")
    print(f"Firmware: {cc.firm}")
    
    # Check if zero calibration needed
    if cc.getNeedsCalibrateZero():
        print("Cover the sensor and calibrate...")
        # cc.calibrateZero()
    
    # Take a measurement
    ok, X, Y, Z = cc.measure()
    if ok:
        print(f"Luminance: {Y} cd/m²")
else:
    print("Connection failed")

# %% 
