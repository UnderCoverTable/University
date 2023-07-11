  void display(int arr[]);
  void populateArray(int arr[]);
  float getDecimalValue(int arr[]);
  void getComplement(int arr[]);
  int getBitPos();
  int readBit(int);
  float dec;

  int siz = 5;
  int arr[] = {0,0,0,0,0};
  int complArr[5];


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println("\t====== LAB 01 ======");
  Serial.println();

  
  populateArray(arr);
  display(arr);
  float out = getDecimalValue(arr);

  Serial.print("Decimal value of this binary number is: ");
  Serial.println(out);
  Serial.print("Complement of given binary number is: ");
  getComplement(arr);
  display(complArr);
  Serial.println("Enter a bit position(Starting from the LS bit): ");
  int pos = getBitPos();

  if (pos >= 5)
  {
    Serial.println("Invalid bit position !");
  }
  else
  {
    Serial.print(pos);
    Serial.print(" is: ");
    int val = readBit(pos);
    Serial.println(val);
  }
}

void loop() {
  // put your main code here, to run repeatedly:
}

int readBit(int p){

  return arr[p];
}

int getBitPos(){

  while (Serial.available()==0){} 
  int inputIndex;

  inputIndex = Serial.parseInt();
  Serial.println(inputIndex);
  return inputIndex;



}

void getComplement(int arr[5]){

  int i  = 4;

  while (i >= 0){
    if (arr[i] == 1){
      complArr[i] = 0;
    }
    else{
      complArr[i] = 1;
    }
    i--;
  }  



}

float getDecimalValue(int arr[5]){

  int i = 0;
  while (i<5){
    dec += arr[i] * pow(2, i);
    i++;
    }
    return dec;

}

void populateArray(int arr[5]){

  int inputBin;
  Serial.println("Enter 5 bit bianry number:  ");        //Prompt User for input
  while (Serial.available()==0){}             // wait for user input
  inputBin = Serial.parseInt();                    //Read user input and hold it in a variable
 

  int i = 0;
  int digit;
  while(inputBin) {
      digit = inputBin % 10;
      inputBin /= 10;

      arr[i] = digit;
      i++;
      
  }

  // i = 4;
  // while(i >= 0){

  //   Serial.print(arr[i]);
  //   i--;
  // }
  //     Serial.println();




}

void display(int arr[5]){
   int i = 4;
  while(i >= 0){

    Serial.print(arr[i]);
    i--;
  }
      Serial.println();

}