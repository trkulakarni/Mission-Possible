void setup() {
  pinMode(A5,INPUT);
  pinMode(A1,OUTPUT);
  pinMode(A0,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int LDR=analogRead(A5);
  Serial.println(LDR);
  if(LDR>800) {analogWrite(A1,160);analogWrite(A0,160);}
  else if (100<LDR<800){analogWrite(A1,160);analogWrite(A0,0);}
  else if (20<LDR<100){analogWrite(A1,0);analogWrite(A0,160);}
  else {analogWrite(A1,0);analogWrite(A0,0);} 
  delay(1000);
  
}

