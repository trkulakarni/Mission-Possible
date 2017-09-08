void setup()
{pinMode(7, INPUT);}

Serial.begin(9600);}
void loop()
{
int PIR=  digitalRead(7);

Serial.println(PIR);
delay(500);
}

