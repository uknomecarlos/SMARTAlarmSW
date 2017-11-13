from PointOfInterest import *
from path import *
from xbee import ZigBee
from WirelessFunctions import *
import time
import serial
import Queue
import termios, fcntl, sys, os


fd = sys.stdin.fileno()

oldterm = termios.tcgetattr(fd)
newattr = termios.tcgetattr(fd)
newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
termios.tcsetattr(fd, termios.TCSANOW, newattr)

oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

# on the Raspberry Pi the serial port is ttyAMA0
PORT = '/dev/serial0'
#PORT = '/dev/ttyAMA0'
BAUD_RATE = 9600

# Open serial port
ser = serial.Serial(PORT, BAUD_RATE)

# Set up a queue to hold all incoming packets
packets = Queue.Queue()

# Create array of POI and set up alarm layout
def set_poi(my_poi, vis, num_alarm, num_exit):

    # set up POI as wall, it's a placeholder, to place walls adjacent to alarms
    my_poi += [PointOfInterest(0, "wall")]

    # Set up five POIs as type alarm
    for i in range(1, num_alarm + 1):
        temp_poi = PointOfInterest(i, "alarm")
        my_poi += [temp_poi]

    # Set up 2 POIs as type exit
    for i in range(num_alarm + 1, num_alarm + num_exit + 1):
        my_poi += [PointOfInterest(i, "exit")]

    for poi in my_poi:
        vis += [False]

# sts the wireless addresses for all 5 alarms
def set_addresses(all_pois):
    # This is set according to the address of the xbee router
    # connected to each alarm
    all_pois[1].set_address('\x00\x13\xa2\x00\x41\x67\x19\x2c') 
    all_pois[2].set_address('\x00\x13\xa2\x00\x41\x74\x20\xa9') 
    all_pois[3].set_address('\x00\x13\xa2\x00\x41\x74\x20\xb1') 
    all_pois[4].set_address('\x00\x13\xa2\x00\x41\x74\x20\xa5') 
    all_pois[5].set_address('\x00\x13\xa2\x00\x41\x74\x20\xbb')  

# this is a call back function.  When a message
# comes in this function will get the data
def message_received(data):
        packets.put(data, block=False)
        print 'gotta packet'
        
def test_case3(zb):
    # 5 alarms, L Shape, exit on either side, top alarm (1) detects fire
    # From Fig. 48 (p. 117) in "SMART Alarm System SD1 Documentation.pdf

    all_pois = []  # list containing every POI in system
    visited = []  # a boolean value corresponding to each POI and it's ID

    set_poi(all_pois, visited, 5, 2)
    wall = all_pois[0]
    set_addresses(all_pois)

    # initialize the connections from one alarm to another
    all_pois[1].set_all(all_pois[2], wall, all_pois[6])
    all_pois[2].set_all(all_pois[3], wall, all_pois[1])
    all_pois[3].set_all(wall, all_pois[4], all_pois[2])
    all_pois[4].set_all(all_pois[3], wall, all_pois[5])
    all_pois[5].set_all(all_pois[4], wall, all_pois[7])

    print " "
    print "Test Case 3: "
    print " "


    try:
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
                            handlePacket(newPacket, all_pois, visited, zb)
            except KeyboardInterrupt:
                    break
            try:
                c = sys.stdin.read(1)
                print "Got character", repr(c)
                if c == 'r':
                    signalReset(zb, all_pois)
            except IOError: pass
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
    
    # halt() must be called before closing the serial
    # port in order to ensure proper thread shutdown
    zb.halt()
    ser.close()#!/usr/bin/python
    
# main function
def main():

    # Create XBee library API object, which spawns a new thread
    zb = ZigBee(ser, callback=message_received)
    print 'starting'
    
    test_case3(zb)


if __name__ == "__main__":
    main()
