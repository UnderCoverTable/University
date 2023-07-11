int ldr=A0;//Set A0(Analog Input) for LDR.
int value=0;
void setup() {
Serial.begin(9600);
pinMode(3,OUTPUT);
}

void loop() {
value=analogRead(ldr);//Reads the Value of LDR(light).
Serial.println(value);
if(value<250)
  {
    digitalWrite(3,HIGH);//Makes the LED glow in Dark.
  }
  else
  {
    digitalWrite(3,LOW);//Turns the LED OFF in Light.
  }
}