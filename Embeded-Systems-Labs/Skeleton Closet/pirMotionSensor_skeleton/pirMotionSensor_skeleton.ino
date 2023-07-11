const int Motion = 3;
const int led = 4;
int val = 0;
int state = LOW;

void setup() {
  // put your setup code here, to run once:
  pinMode(Motion, INPUT);
  pinMode(led,OUTPUT);  // led
  Serial.begin(9600);
}

void loop() {
  digitalWrite(led,LOW);
  // put your main code here, to run repeatedly:
  val = digitalRead(Motion);
//  delay(100);
  if(val == HIGH){
    digitalWrite(led, HIGH);  
    if(state == LOW){
      Serial.println("Motion!");
      state = HIGH;
    }
  }
  else{
      digitalWrite(led, LOW);  
      if(state == HIGH){
      Serial.println("Motion stopped!");
      state = LOW;
    }
    }
}