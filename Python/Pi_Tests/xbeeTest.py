#! /usr/bin/python
# This is an example of asyncronous receive
# What it actually does is fork off a new process
# to do the XBee receive.  This way, the main
# code can go do somthing else and hand waiting
# for the XBee messages to come in to another
# process.

from xbee import ZigBee
from apscheduler.scheduler import Scheduler
import time
import serial
import Queue

# on the Raspberry Pi the serial port is ttyAMA0
#PORT = '/dev/serial0'
PORT = '/dev/ttyAMA0'
BAUD_RATE = 9600

# The XBee addresses I'm dealing with
BROADCAST = '\x00\x13\xa2\x00\x41\x67\x19\x2c'
UNKNOWN = '\xff\xfe' # This is the 'I don't know' 16 bitA address


packets = Queue.Queue()

# Open serial port
ser = serial.Serial(PORT, BAUD_RATE)

# this is a call back function.  When a message
# comes in this function will get the data
def message_received(data):
        packets.put(data, block=False)
        print 'gotta packet'

def sendPacket(where, what):
        # I'm only going to send the absolute minimum.
        zb.send('tx',
                dest_addr_long = where,
                # I always use the 'unknown' value for this
                # it's too much trouble to keep track of two
                # addresses for the device
                dest_addr = UNKNOWN,
                data = what)

# In my house network sending a '?\r' (question mark, carriage
# return) causes the controller to send a packet with some status
# information in it as a broadcast.  As a test, I'll send it and
# the receive above should catch the response.
def sendQueryPacket():
        # I'm broadcasting this message only
        # because it makes it easier for a monitoring
        # XBee to see the packet.  This is a test
        # module, remember?
        print 'sending query packet'
        sendPacket(BROADCAST, 'left')

# OK, another thread has caught the packet from the XBee network,
# put it on a queue, this process has taken it off the queue and
# passed it to this routine, now we can take it apart and see
# what is going on ... whew!
def handlePacket(data):
        print 'In handlePacket: ',
        print data['id'],
        if data['id'] == 'tx_status':
                print data['deliver_status'].encode('hex')
        elif data['id'] == 'rx':
                print data['source_addr_long'].encode('hex')
                print data['rf_data']
        else:
                print 'Unimplemented frame type'


# Create XBee library API object, which spawns a new thread
zb = ZigBee(ser, callback=message_received)

sendsched = Scheduler()
sendsched.start()

# every 30 seconds send a house query packet to the XBee network
sendsched.add_interval_job(sendQueryPacket, seconds=30)

# Do other stuff in the main thread
while True:
        try:
                time.sleep(0.1)
                if packets.qsize() > 0:
                        print "got somethin"
                        # got a packet from recv thread
                        # See, the receive thread gets them
                        # puts them on a queue and here is
                        # where I pick them off to use
                        newPacket = packets.get_nowait()
                        # now go dismantle the packet
                        # and use it.
                        handlePacket(newPacket)
        except KeyboardInterrupt:
                break

# halt() must be called before closing the serial
# port in order to ensure proper thread shutdown
zb.halt()
ser.close()#!/usr/bin/python
import serial
from xbee import ZigBee

serial_port = serial.Serial('/dev/ttyAMA0', 9600)

zb = ZigBee(serial_port)

print "hello"
while True:
    try:
        data = zb.wait_read_frame() #Get data for later use
        #print data # for debugging only
        print data['rf_data']

    except KeyboardInterrupt:
        break

serial_port.close()
