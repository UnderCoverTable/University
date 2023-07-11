int ports[4] = {2,3,4,5};
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  for(int i=0; i<5; i++){
    pinMode(ports[i], OUTPUT);
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  for(int j=4; j>=0; j--){
    delay(200);
    digitalWrite(ports[j], HIGH);
    delay(200);
  }
 
  for(int i=0; i<4; i++){
    delay(200);
       for(int j=0; j<5; j++){
        digitalWrite(ports[j], HIGH);
        }
        delay(200);
       for(int k=0; k<5;k++){
        digitalWrite(ports[k], LOW);
        }
        delay(200);
    }
    
  
   for(int j=0; j<5; j++){
    delay(200);
    digitalWrite(ports[j], HIGH);
    delay(200);
  }
   for(int k=0; k<5;k++){
        digitalWrite(ports[k], LOW);
   }
  
}
