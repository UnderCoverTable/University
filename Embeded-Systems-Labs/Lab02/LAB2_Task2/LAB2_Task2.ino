
String inp = "";
int j=0;
int count;
bool check = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

    pinMode(2, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  
  while(Serial.available() == 0){}

    inp = Serial.readStringUntil('$');
  while(j != inp.length()){
    if(inp[j] != ' '){
      count++;
    }
    j++;
  }
  if(inp.length()>0){
    check = 1;
    }

  Serial.println(count);
  for(int i=0; i<count; i++){
    delay(500);
    digitalWrite(2, HIGH);
    delay(500);
    digitalWrite(2, LOW);
    }
    digitalWrite(2,LOW);
    

   while(1);
}
