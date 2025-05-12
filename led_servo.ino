#include <Servo.h>

const int ledPin = 13;      
const int servoPin = 9;     
Servo myServo;

bool ledState = false;
unsigned long previousMillis = 0;
const long interval = 1000;

int angle = 0;
int step = 1;

void setup() {
  pinMode(ledPin, OUTPUT);
  myServo.attach(servoPin);
  myServo.write(angle);
}

void loop() {
  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;
    ledState = !ledState;
    digitalWrite(ledPin, ledState);
  }

  myServo.write(angle);
  angle += step;
  if (angle >= 180 || angle <= 0) {
    step = -step; 
  }
  delay(15);
}
