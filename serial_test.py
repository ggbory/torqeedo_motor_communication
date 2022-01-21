#!/usr/bin/env python

import serial
import crc8

ser = serial.Serial(port='/dev/ttyUSB0',baudrate = 19200,parity=serial.PARITY_NONE,\
                    stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=0)

def hexshow(data):

    hex_data = '' hLen = len(data)

    for i in xrange(hLen):
        hvo1 = ord(data[i])
        hhex = '%02x' % hvo1
        hex_data += hhex + ' '

    print 'hexSHow:',result

print("connected to :"+ser.portstr)

pkg = "0xAC0x300x00"
hash = crc8.crc8()
hash.update(pkg.encode('utf-8'))
print(hash.hexdigest())

#ser.write("0xAC0x800x000x2C0xAD")

ser.write("0xAC0x300x000x2C0xAD")
    #print('send')
line=ser.readlines()
print(line)

ser.close()