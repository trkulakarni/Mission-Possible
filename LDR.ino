void setup() {
  pinMode(A5,INPUT);
  Serial.begin(9600);
}

void loop() {
  int LDR=analogRead(A5);
  Serial.println(LDR);
  delay(1000);
}
