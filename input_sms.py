


import serial
#ser = serial.Serial(port='/dev/ttyUSB1', baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=1, xonxoff=False, rtscts=False, dsrdtr=False)
ser = serial.Serial("/dev/ttyUSB1", baudrate=115200, timeout=3.0)

cmd="AT+CMGF=1\r"
print ser.write(cmd.encode())
msg=ser.read(64)
print(msg)

while True:
    
    ser.write("AT+CMGL\r\n".encode())
    result = ser.read(64).split(",")
    print len(result), result
    if len(result) == 6:
        print result[2]
        gpio_path = '/sys/class/gpio_sw/PA1/data'
        open(gpio_path,'w').write(str(1))
        open(gpio_path,'w').write(str(0))
#modem = serial.Serial('/dev/ttyUSB1', 460800, timeout=5, xonxoff = False, rtscts = False, bytesize = serial.EIGHTBITS, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE)          
#modem.write('AT+CMGF=1\r')
#print modem.write('AT+CMGL\r')
#print modem.read(2)
#modem.close()
