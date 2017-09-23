/*
XBee TX test for a Arduino Mega2560 using Serial3 as the XBee serial
input for a Series 2 XBee.  This is NOT based on the examples that come with
the Arduino XBee library.

See, the examples there and most other places on the web SUCK.  Andrew's
library is much easier to use than the illustrations would lead you to believe.

This is a HEAVILY commented example of how send a text packet using series 2
XBees.  Series 1 XBees are left as an exercise for the student.
*/

#include <XBee.h>

XBee xbee = XBee();
// This is the XBee broadcast address.  You can use the address
// of any device you have also.
XBeeAddress64 Broadcast = XBeeAddress64(0x0013A200, 0x41496656);

char Hello[] = "Hello World";
char Buffer[128];  // this needs to be longer than your longest packet.

void setup() { 
  // start serial
  Serial.begin(9600);
  // now that they are started, hook the XBee into
  // Software Serial
  xbee.setSerial(Serial);
  Serial.println("Initialization all done!");
}

void loop() {
  strcpy(Buffer, "Hello World");
  ZBTxRequest zbtx = ZBTxRequest(Broadcast, (uint8_t *)Hello, strlen(Hello));
  xbee.send(zbtx);
  delay(30000);
  strcpy(Buffer,"I saw what you did last night.");
  zbtx = ZBTxRequest(Broadcast, (uint8_t *)Buffer, strlen(Buffer));
  xbee.send(zbtx);
  delay(30000);
}

void handleXbeeRxMessage(uint8_t *data, uint8_t length){
  // this is just a stub to show how to get the data,
  // and is where you put your code to do something with
  // it.
  for (int i = 0; i < length; i++){
//    Serial.print(data[i]);
  }
//  Serial.println();
}

void showFrameData(){
  Serial.println("Incoming frame data:");
  for (int i = 0; i < xbee.getResponse().getFrameDataLength(); i++) {
    print8Bits(xbee.getResponse().getFrameData()[i]);
    Serial.print(' ');
  }
  Serial.println();
  for (int i= 0; i < xbee.getResponse().getFrameDataLength(); i++){
    Serial.write(' ');
    if (iscntrl(xbee.getResponse().getFrameData()[i]))
      Serial.write(' ');
    else
      Serial.write(xbee.getResponse().getFrameData()[i]);
    Serial.write(' ');
  }
  Serial.println(); 
}

// these routines are just to print the data with
// leading zeros and allow formatting such that it
// will be easy to read.
void print32Bits(uint32_t dw){
  print16Bits(dw >> 16);
  print16Bits(dw & 0xFFFF);
}

void print16Bits(uint16_t w){
  print8Bits(w >> 8);
  print8Bits(w & 0x00FF);
}

void print8Bits(byte c){
  uint8_t nibble = (c >> 4);
  if (nibble <= 9)
    Serial.write(nibble + 0x30);
  else
    Serial.write(nibble + 0x37);
      
  nibble = (uint8_t) (c & 0x0F);
  if (nibble <= 9)
    Serial.write(nibble + 0x30);
  else
    Serial.write(nibble + 0x37);
}
