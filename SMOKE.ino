void setup() {pinMode(7,INPUT);
Serial.begin(9600);
}

void loop() {
  int SMOKE= digitalRead(7);
  if(SMOKE==1)analogWrite(A0,160);
  else if (SMOKE==0) analogWrite(A0,0);
  
  Serial.println(SMOKE);
  delay(500);
 

}
