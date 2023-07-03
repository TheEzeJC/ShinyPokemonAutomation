// include the Servo library
#include <Servo.h>

// create servo object
Servo servoButton;

bool keepLooping = true;
int defaultPosition = 90;

void setup() {
  servoButton.write(defaultPosition); //starting angle
  servoButton.attach(9); // attaches the servo on pin 9 to the servo object
  
  Serial.begin(9600); // open a serial connection to your computer
}

void pressAButton(int pressDurationInMS) {
  servoButton.write(117); // set servo push down angle
  delay(pressDurationInMS);   // wait
  servoButton.write(defaultPosition); // reset servo angle
}

void pressStartButton(int pressDurationInMS) {
  servoButton.write(70); // set servo push down angle
  delay(pressDurationInMS);   // wait
  servoButton.write(defaultPosition); // reset servo angle
}

void loop() {
  pressStartButton(400);
  delay(30000);
}