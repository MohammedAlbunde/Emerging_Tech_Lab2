import serial
import time
from datetime import datetime
arduino = serial.Serial(port='COM11', baudrate=9600, timeout=1)
import csv
def write_read(x):
    arduino.flushInput()
    arduino.flushOutput()
    time.sleep(1.05)
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data
namesArray = ["TimeStamp","TemperatureValue","Sensor","Frequncy"]
f = open('record.csv','a')
writer =csv.writer(f)
writer.writerow(namesArray) 
f.close()
time.sleep(3)
while True:
    tempArray = [] 
    f = open('record.csv','a')
    writer =csv.writer(f)
    datetime = time.ctime()
    value = write_read(str(1))
    
    
    
    tempArray.append(datetime)
    tempArray.append(str(value)[2:-7])
    tempArray.append("MCP 9700AE")
    tempArray.append("1")
    writer.writerow(tempArray) 
    f.close()

    

 #  time.sleep(1)