#!/usr/bin/python
import serial
from xbee import ZigBee

serial_port = serial.Serial('/dev/ttyS0', 9600)

zb = ZigBee(serial_port)

print "starting"
while True:
    try:
        data = zb.wait_read_frame() #Get data for later use
        #print data # for debugging only
        print "got something"
        print data['rf_data']

    except KeyboardInterrupt:
        break

serial_port.close()
