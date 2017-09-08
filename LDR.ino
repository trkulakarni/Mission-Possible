void setup() {
  pinMode(A0,INPUT);
  Serial.begin(9600);
}

void loop() {
  int LDR=analogRead(A0);
  Serial.println(LDR);
  if(LDR>800) {analogWrite(A1,160);analogWrite(A0,160);}
  else if (300<LDR<800){analogWrite(A1,160);analogWrite(A0,0);}
  else if (100<LDR<300){analogWrite(A1,0);analogWrite(A0,160);}
  else {analogWrite(A1,0);analogWrite(A0,0);} 
  delay(1000);
  
}

