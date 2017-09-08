int PIR_RPI=A0;
void setup()
{pinMode(7, INPUT);

Serial.begin(9600);}
void loop()
{
int PIR=  digitalRead(7);
if(PIR==1) analogWrite(PIR_RPI,160);
else if (PIR==0) analogWrite(PIR_RPI,0);
Serial.println(PIR);
delay(500);
}

