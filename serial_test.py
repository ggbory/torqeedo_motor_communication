#!/usr/bin/env python

import serial
import crc8
import time

ser = serial.Serial(port='/dev/ttyUSB0',baudrate = 19200,parity=serial.PARITY_NONE,\
                    stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=0)

def hexshow(argv):

    result = ''
    hLen = len(argv)

    for i in xrange(hLen):
        hvo1 = ord(argv[i])
        hhex = '%02x' % hvo1
        result = hhex

    print 'hexSHow:',result

print("connected to :"+ser.portstr)

pkg = "0xAC0x300x820x080x640xAA"
#pkg = "0xAC0x300x01"
hash = crc8.crc8()
hash.update(pkg.encode('utf-8'))
print(hash.hexdigest())

#print(hex(8))
#print(hex(300))
#ser.open()
while True:
    ser.write(b'\xAC\x30\x82\x08\x64\xAA\x98\xAD')
    time.sleep(5)
    #for line in ser.readline():
        #print(hexshow(line))


#ser.write("0xAC0x300x000x2C0xAD")

#ser.write("0xAC0x300x000x2C0xAD")
    #print('send')
#line=ser.readlines()
#print(line)

ser.close()