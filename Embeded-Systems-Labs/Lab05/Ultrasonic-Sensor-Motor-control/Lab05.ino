int echoPin = 2;

int pwm = 9;
long pwm_speed;

long startTime = 0;
int distKeep;
bool flag = false;

long duration; // variable for the duration of sound wave travel
int distance; // variable for the distance measurement

void setup(){

  DDRD = B11101000; // Turn pin 2,6,7 to Output and 3 to input
  DDRB = B00000010; // Turn pin 9 to output

  PORTD = B01000000; // Turn pin 6 high and pin 7 low
  
  Serial.begin(9600);
}

void loop(){

  PORTD = B01000000; // pin 3 low
  delayMicroseconds(2);

  PORTD = B01001000; // pin 3 high

  delayMicroseconds(10);
  PORTD = B01000000; // pin 3 low

  duration = pulseIn(echoPin, HIGH);

  distance = duration * 0.034 / 2;  // Sonar distance reading

  if(flag == false){    // flag setup to fix millis() getting the distance 0
    distKeep = distance;
  }
  flag = !flag;


  pwm_speed = map(distance,5,20,0,255); // Set speed according to the sonars distance 

  if(distance > 20){  
      pwm_speed = 255;
  }
  
  if(distance < 5){
      pwm_speed = 0;
  }
  
  analogWrite(pwm,pwm_speed);

  if(distance == 0){
    distance = distKeep;
  }

  if(millis() - startTime >= 3000){
    startTime = millis();

    Serial.print("Distance: ");
    Serial.print(distance);
    Serial.println(" cm");
  }

}