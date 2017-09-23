#include <XBee.h>

XBee xbee = XBee();
// This is the XBee broadcast address.  You can use the address
// of any device you have also.
XBeeAddress64 Broadcast = XBeeAddress64(0x0013A200, 0x41496656);

char left[] = "left";
char right[] = "right";
void setup() {
  Serial.begin(9600);
  // now that they are started, hook the XBee into
  // Software Serial
  xbee.setSerial(Serial);
  Serial.println("Initialization all done!");
}

void loop() {
  // put your main code here, to run repeatedly:
  
  ZBTxRequest zbtx = ZBTxRequest(Broadcast, (uint8_t *)left, strlen(left));
  xbee.send(zbtx);
  delay(30000);
  zbtx = ZBTxRequest(Broadcast, (uint8_t *)right, strlen(right));
  xbee.send(zbtx);
  delay(30000);
}
