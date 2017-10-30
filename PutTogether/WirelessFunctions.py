from xbee import ZigBee
from twilio.rest import Client
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import serial
from PointOfInterest import *
from path import *


UNKNOWN = '\xff\xfe' # This is the 'I don't know' 16 bitA address

# Setup sms text client with specified account details
client = Client("AC591080d05afb9ed3ce18caa8217357b9","b373738564ac52c3cb981a14676f1d63")

smsReceiver = "+17278719771"
smsSender = "+13059129032"

# Setup email settings for the smart alarm emergency messages
fromaddr = 'smartalarmucf@yahoo.com'
password = 'goknights'
toaddr = 'lplager@icloud.com'
smtp = 'smtp.mail.yahoo.com'
port = 587


def sendPacket(zb, where, what):
        # I'm only going to send the absolute minimum.
        zb.send('tx',
                dest_addr_long = where,
                # I always use the 'unknown' value for this
                # it's too much trouble to keep track of two
                # addresses for the device
                dest_addr = UNKNOWN,
                data = what) 

# Cycle through all the alarms and send the proper direction signal
def signalDirections(zb, all_pois):
        print 'length = ', len(all_pois)
        for i in range(0, len(all_pois)-4):
                for poi in all_pois:
                        if poi.get_distance() == i:
                                time.sleep(0.005)    
                                if poi.get_type() != "exit" and poi.get_type() != "wall":
                                        sendPacket(zb, poi.get_address(), poi.get_next_direction())
                time.sleep(1)
                print i
                
# Cycle through all the alarms and send the reset signal
def signalReset(zb, all_pois):
        for poi in all_pois:
                time.sleep(0.005)    
                if poi.get_type() != "exit" and poi.get_type() != "wall":
                        sendPacket(zb, poi.get_address(), 'reset')

# Send an email packet
def sendEmail(alarmID):
        server = smtplib.SMTP(smtp, 587)
        server.ehlo
        server.starttls()
        server.login(fromaddr, password)

        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Emergency SmartAlarm Alert!"
        body = ('The SmartAlarm system has detected a fire emergency at alarm ' + alarmID + '. Alarms have been triggered!')

        msg.attach(MIMEText(body, 'plain'))

        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()

# OK, another thread has caught the packet from the XBee network,
# put it on a queue, this process has taken it off the queue and
# passed it to this routine, now we can take it apart and see
# what is going on ... whew!
def handlePacket(data, all_pois, visited, zb):
        print 'In handlePacket: ',
        print data['id'],
        if data['id'] == 'tx_status':
                print data['deliver_status'].encode('hex')
        elif data['id'] == 'rx':
                print '\naddress is:',
                print data['source_addr_long'].encode('hex')
                print data['rf_data'],'\n'
                poi = find_alarm_with_address(all_pois, data['source_addr_long'])
                if(poi != False):
                        reset_alarms(all_pois, visited)
                        fire_alarm(poi, visited)
                        print_each_direction(all_pois)
                        signalDirections(zb, all_pois)
                        client.messages.create(to=smsReceiver, from_=smsSender, body="There is a fire at alarm " + str(poi.get_id()) + "!!!")
                        sendEmail(str(poi.get_id()))
        else:
                print 'Unimplemented frame type'
