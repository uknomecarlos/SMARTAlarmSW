#include <XBee.h>

XBee xbee = XBee();
XBeeResponse response = XBeeResponse();
// create reusable response objects for responses we expect to handle
ZBRxResponse rx = ZBRxResponse();
ZBRxIoSampleResponse ioSample = ZBRxIoSampleResponse();

XBeeAddress64 Broadcast = XBeeAddress64(0x0013A200, 0x41496656);

char left[] = "left";
char right[] = "right";
char test[128] = "left";
const int buttonPin = 9;

int previous = LOW;
int reading;
bool state = true;

long time = 0;
long debounce = 3000;
ZBTxRequest zbtx;

void setup() {
  Serial.begin(9600);
  xbee.setSerial(Serial);

  pinMode(buttonPin, INPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  // I think this is the only line actually left over
  // from Andrew's original example
  //Serial.println("starting up yo!");
}

void loop() {

    if(millis() - time > debounce){
      if (state == true){
        state = false;
        zbtx = ZBTxRequest(Broadcast, (uint8_t *)left, strlen(left));
        xbee.send(zbtx);
      }
      else {
        state = true;
        zbtx = ZBTxRequest(Broadcast, (uint8_t *)right, strlen(right));
        xbee.send(zbtx);
      }
      time = millis();
    }
  
  // doing the read without a timer makes it non-blocking, so
    // you can do other stuff in loop() as well.
    xbee.readPacket();
    // so the read above will set the available up to
    // work when you check it.
    if (xbee.getResponse().isAvailable()) {
      // got something
      // I commented out the printing of the entire frame, but
      // left the code in place in case you want to see it for
      // debugging or something.  The actual code is down below.
      //showFrameData();
      //Serial.print("Frame Type is ");
      // Andrew calls the frame type ApiId, it's the first byte
      // of the frame specific data in the packet.
      //Serial.println(xbee.getResponse().getApiId(), HEX);
    
      if (xbee.getResponse().getApiId() == ZB_RX_RESPONSE) {
        // got a zb rx packet, the kind this code is looking for
      
        // now that you know it's a receive packet
        // fill in the values
        xbee.getResponse().getZBRxResponse(rx);

        
        strcpy(test, (char*)rx.getData());
        test[rx.getDataLength()] = 0;
        if(strcmp(test, "left") == 0){
          digitalWrite(5, LOW);
          digitalWrite(6, HIGH);
        } 
        else if (strcmp(test, "right") == 0){
          digitalWrite(5, HIGH);
          digitalWrite(6, LOW);
        }
      }
    }
    else {
      // I hate else statements that don't have some kind
      // ending.  This is where you handle other things
    }
}


