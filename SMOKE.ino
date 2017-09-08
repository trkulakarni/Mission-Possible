void setup() {pinMode(6,INPUT);
Serial.begin(9600);
}

void loop() {
int smoke_detect;
  int SMOKE= digitalRead(6);
  Serial.println(SMOKE);
  delay(500);
 

}
