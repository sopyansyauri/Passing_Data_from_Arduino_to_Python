import time
import serial

arduinoData = serial.Serial("/dev/ttyACM0", 9600)
time.sleep(1)

while True:
    while (arduinoData.inWaiting() == 0):
        pass
    dataPacket = arduinoData.readline()
    dataPacket = str(dataPacket, "utf-8")
    dataPacket = dataPacket.strip("\r\n")
    print(dataPacket)


