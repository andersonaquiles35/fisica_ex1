
#include <Ultrasonic.h>
HC_SR04 US(12,13);

void setup() {
  Serial.begin(9600);
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH);
  while(true){
    Serial.println(US.distance());
    delay(30);
  }
}
