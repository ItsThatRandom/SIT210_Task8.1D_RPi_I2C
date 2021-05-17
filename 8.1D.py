import smbus
import time

# Declare address for our Arduino Slave and create an SMBus object.
slaveAddress = 0x08
bus = smbus.SMBus(1)

# Loop reads data from Arduino and based on value recieved,
# performs appropriate print function. NOTE: All values are
# randomly generated mock values between 0 and 100.
while 1:
    dataNumber = bus.read_byte(slaveAddress)
    if 0 <= dataNumber < 20:
        print("Arduino value recieved is too dark")
    elif 20 <= dataNumber < 40:
        print("Arduino value recieved is dark")
    elif 40 <= dataNumber < 60:
        print("Arduino value recieved is medium")
    elif 60 <= dataNumber < 80:
        print("Arduino value recieved is bright")
    elif 80 <= dataNumber <= 100:
        print("Arduino value recieved is too bright")
    time.sleep(1)