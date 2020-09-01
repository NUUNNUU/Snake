#include <SoftwareSerial.h>

#define BT_RXD 8 // connects to TXD of the bluetooth module
#define BT_TXD 7 // connects to RXD of the bluetooth module

#define mot1PinH 3
#define mot1PinL 4
#define mot2PinH 5
#define mot2PinL 6

SoftwareSerial bluetooth(BT_RXD, BT_TXD);

void setup() {
  Serial.begin(9600);
  bluetooth.begin(9600);
  //pinMode(13, OUTPUT);
  bluetooth.println("Initialize...");
}

void loop() {
  if (bluetooth.available()) {
    char control_flag = bluetooth.read();
    // '0': Forward
    // '1': Turn left
    // '2': Turn right
    // '3': Backward
    Serial.write(control_flag);

    if (control_flag == '1') {
      // go forward
      fwd();
    } else if (control_flag == '2') {
      // turn left
      bwd();
    } else if (control_flag == '3') {
      // turn right
      right();
    } else if (control_flag == '4') {
      // go backward
      left();
    }
    else{
      bluetooth.println("Unidentifed input");
    }
  }
  if (Serial.available()) {
    bluetooth.write(Serial.read());
  }
}

void fwd(){
  bluetooth.print("GOING FORWARD...");
  digitalWrite(mot1PinH, HIGH);
  digitalWrite(mot2PinH, HIGH);
  digitalWrite(mot1PinL, LOW);
  digitalWrite(mot2PinL, LOW);
  delay(5000);
  digitalWrite(mot1PinH, LOW);
  digitalWrite(mot2PinH, LOW);
  bluetooth.println("DONE.");
}

void bwd(){
  bluetooth.print("GOING BACKWARD...");
  digitalWrite(mot1PinH, LOW);
  digitalWrite(mot2PinH, LOW);
  digitalWrite(mot1PinL, HIGH);
  digitalWrite(mot2PinL, HIGH);
  delay(5000);
  digitalWrite(mot1PinL, LOW);
  digitalWrite(mot2PinL, LOW);
  bluetooth.println("DONE.");  
}

void right(){  
  bluetooth.print("GOING RIGHT...");
  digitalWrite(mot1PinH, LOW);
  digitalWrite(mot2PinH, HIGH);
  digitalWrite(mot1PinL, HIGH);
  digitalWrite(mot2PinL, LOW);
  delay(5000);
  digitalWrite(mot1PinL, LOW);
  digitalWrite(mot2PinH, LOW);
  bluetooth.println("DONE.");  
  
}

void left(){
  bluetooth.print("GOING LEFT...");
  digitalWrite(mot1PinH, HIGH);
  digitalWrite(mot2PinH, LOW);
  digitalWrite(mot1PinL, LOW);
  digitalWrite(mot2PinL, HIGH);
  delay(5000);
  digitalWrite(mot1PinH, LOW);
  digitalWrite(mot2PinL, LOW);
  bluetooth.println("DONE."); 
}
