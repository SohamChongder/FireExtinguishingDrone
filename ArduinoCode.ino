#include <Servo.h>

const int servo1Pin = 6; // Pin connected to the first servo
const int servo2Pin = 5; // Pin connected to the second servo

Servo myservo1;
Servo myservo2;

void setup() {
  myservo1.attach(servo1Pin); // Attach the first servo to its pin
  myservo2.attach(servo2Pin); // Attach the second servo to its pin
  
  Serial.begin(9600); // Initialize the serial communication
}

void loop() {
  myservo1.write(0);
  myservo2.write(0);
  
  if (Serial.available()) {
    String myCmd = Serial.readStringUntil('\n');

    if (myCmd == "1") {
      myservo1.write(90); // Set the first servo position to 90 degrees
      myservo2.write(90); // Set the second servo position to 90 degrees
      
      Serial.println("Servos turned on");
    } else {
      myservo1.write(0); // Set the first servo position to 0 degrees
      myservo2.write(0); // Set the second servo position to 0 degrees
      
      Serial.println("Servos turned off");
    }
  }
  
  delay(500);
}

