#include <Wire.h>

long randomInteger;

void setup() {
  // Connect to I2C as a slave at a given address
  Wire.begin(0x8);

  Wire.onRequest(fakeData);
}

//
void fakeData()
{
  randomInteger = random(100);
  Wire.write(randomInteger);
}
void loop() {
  // simply delays, waiting for I2C requests from RPI.
  delay(100);
}
