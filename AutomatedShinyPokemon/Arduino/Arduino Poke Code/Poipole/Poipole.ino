// include the Servo library
#include <Servo.h>

// create servo object
Servo servoButton;

bool keepLooping = true;
int defaultPosition = 90;

// connect servo
void setup() {
  servoButton.write(defaultPosition); //starting angle
  servoButton.attach(9); // attaches the servo on pin 9 to the servo object
  
  Serial.begin(9600); // open a serial connection to your computer
}

// press A function
void pressAButton(int pressDurationInMS) {
  servoButton.write(120); // set servo push down angle
  delay(pressDurationInMS);   // wait
  servoButton.write(defaultPosition); // reset servo angle
}

// press Start funtiin
void pressStartButton(int pressDurationInMS) {
  servoButton.write(70); // set servo push down angle
  delay(pressDurationInMS);   // wait
  servoButton.write(defaultPosition); // reset servo angle
}

void loop() {
  delay(5000); // wait 5 seconds before starting

  if (keepLooping) {
    Serial.println("Starting Loop");
    Serial.println("Skipping Fluff");

    //skip dialog
    {
    //menu cutscene
      pressAButton(300);
      delay(3000);

      //menu
      pressAButton(300);
      delay(3000);

      //Message 1
      pressAButton(300);
      delay(2000);
      //Message 2
      pressAButton(300);
      delay(700);
      //Message 3
      pressAButton(300);
      delay(700);
      //Message 4
      pressAButton(300);
      delay(700);
      //Message 5
      pressAButton(300);
      delay(5000);
      //Message 6
      pressAButton(300);
      delay(700);
    }

    Serial.println("Finished Dialog");
    delay(2500); //delay so image can be taken properly and not the cutscene transition

    // Send message to Python
    Serial.println("Command: checkIfShiny");

    // Wait until we receive a message from Python
    while (Serial.available() == 0) {
      delay(100);
    }
    Serial.println("Reading response from Python");
    // Read response from Python
    char inByte = Serial.read();

    //Read Program Code and translate to Arduino
    if (inByte == 'y') {
      // it's shiny! Stop looping
      Serial.println("It's shiny!");
      keepLooping = false;
    } else {
      // Do a soft reset and keep on looping!
      Serial.println("Not shiny. Doing soft reset");
      keepLooping = true;
      pressStartButton(400);

      // wait 6 seconds after soft reset to let game load
      delay(6000);
    }
  }
}