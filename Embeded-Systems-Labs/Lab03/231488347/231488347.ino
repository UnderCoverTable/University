#include <Keypad.h>

int ledPin = 2;
int actLed = 13;
char keypadInp[6];
int numOfLitres = 0;
int blink = 0;

int inpCounter = 0;
int i = 0;

const byte ROWS = 4; //four rows
const byte COLS = 3; //three columns
char keys[ROWS][COLS] = {
  {'1', '2', '3'},
  {'4', '5', '6'},
  {'7', '8', '9'},
  {'*', '0', '#'}
};

byte rowPins[ROWS] = {6,7,8,9}; //connect to the row pinouts of the keypad
byte colPins[COLS] = {10,11,12}; //connect to the column pinouts of the keypad
Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );
void setup(){
 Serial.begin(9600);
 pinMode(ledPin,OUTPUT);
 pinMode(actLed,OUTPUT);

  Serial.println("Initializing. Please wait...");
   for(i; i != 6; i++){
    digitalWrite(actLed,HIGH);
    delay(400);
    digitalWrite(actLed,LOW);
    delay(400);
  }


  Serial.print("Please Enter The Amount Of Fuel: ");

}

void loop(){


  char key = keypad.getKey();

  if (key != NO_KEY){
    if(key == '#'){
    //Serial.println(keypadInp);
    //Serial.println(inpCounter);

    int inInt;
    inInt = atoi(keypadInp);

  
    numOfLitres = inInt / 200;
    Serial.println();
    Serial.print(numOfLitres);
    if(numOfLitres < 1){
      Serial.println("We Cannot Dispense This Amount Of Fuel");
      Serial.println("Thank You For Visitng");
      while(1);
    }
    Serial.println("L Will be filled");

    delay(1000);

    Serial.println("Dispensing Fuel Please Wait..");
    for(blink; blink != numOfLitres; blink++){
        digitalWrite(ledPin,HIGH);
        delay(400);
        digitalWrite(ledPin,LOW);
        delay(400);
        digitalWrite(ledPin,HIGH);
        delay(400);
        digitalWrite(ledPin,LOW);
        delay(400);
        digitalWrite(ledPin,HIGH);
        delay(400);
        digitalWrite(ledPin,LOW);
        delay(800);
        
    }
      Serial.println("Thank you for visitng us");
      Serial.println();
      while(1);
      
  }
  else{
    Serial.print(key);
    keypadInp[inpCounter] = key;
    inpCounter++;
  }

 
  }

}