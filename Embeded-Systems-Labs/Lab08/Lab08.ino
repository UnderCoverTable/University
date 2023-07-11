
#include <WiFi.h>
#include <WebServer.h>

 
// Replace with your network credentials
const char* ssid     = "Me";
const char* password = "12345678";
 
WebServer server(80);   //instantiate server at port 80 (http port)
 
//String page = "";
int LEDPin = 33;
int numOfBlinks = 0;
int delayMS = 0;

//create web page
String getpage()
{
  String page = "<h1>Simple NodeMCU Web Server</h1>";

  page += "Choose Number of Blinks: ";
  page += "<select onChange='window.location.href=this.value'>";
  page += "  <option value= ''> </option>";
  page += "  <option value= '2blinks\'>2</option>";
  page += "  <option value= '4blinks\'>4</option>";
  page += "  <option value= '6blinks\'>6</option>";
  page += "  <option value= '8blinks\'>8</option>";
  page += "</select>";

  page += "<br><br>";

  page += "Select delay in Ms: ";
  page += "<select onChange='window.location.href=this.value'>";
  page += "  <option value= ''> </option>";
  page += "    <option value='500ms\'>500</option>";
  page += "    <option value='1000ms\'>1000</option>";
  page += "    <option value='1500ms\'>1500</option>";
  page += "    <option value='2000ms\'>2000</option>";
  page += "</select>";
  page += "<br><br>";


  page += "<form action='\startBlinking'>";
  page += "<button type='submit'>Submit</button>";
  page += "</form>";


  
  return page;
  
}



void setup(void){
  
  //make the LED pin output and initially turned off
  pinMode(LEDPin, OUTPUT);
  digitalWrite(LEDPin, LOW);
   
  delay(1000);
  Serial.begin(9600);
  WiFi.begin(ssid, password); //begin WiFi connection
  Serial.println("");
 
  // Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  server.on("/",handle_Root);
  server.on("/2blinks",handle_2blinks);
  server.on("/4blinks",handle_4blinks);
  server.on("/6blinks",handle_6blinks);
  server.on("/8blinks",handle_8blinks);

  server.on("/500ms",handle_500msDelay);
  server.on("/1000ms",handle_1000msDelay);
  server.on("/1500ms",handle_1500msDelay);
  server.on("/2000ms",handle_2000msDelay);

  server.on("/startBlinking",handle_startBlinking);



  server.begin();
  Serial.println("Web server started!");
  
}
 
void loop(void){
  server.handleClient();
}

void handle_Root()
{
  server.send(200, "text/html", getpage());
}

void handle_startBlinking()
{
  server.send(200, "text/html", getpage());

  Serial.print("Blinking LED ");
  Serial.print(numOfBlinks);
  Serial.print(" Times with ");
  Serial.print(delayMS);
  Serial.println(" Ms delay");

  for(int i = 1; i <= numOfBlinks; i++){
    digitalWrite(LEDPin,HIGH);
    delay(delayMS);
    digitalWrite(LEDPin,LOW);
    delay(delayMS);
  }
  
  delay(1000);

}


void handle_2blinks()
{
  server.send(200, "text/html", getpage());
  Serial.println("2blinks");
  numOfBlinks = 2;
  delay(1000);
}

void handle_4blinks()
{
  server.send(200, "text/html", getpage());
  Serial.println("4blinks");
  numOfBlinks = 4;
  delay(1000);
}

void handle_6blinks()
{
  server.send(200, "text/html", getpage());
  Serial.println("6blinks");
  numOfBlinks = 6;
  delay(1000);
}
void handle_8blinks()
{
  server.send(200, "text/html", getpage());
  Serial.println("8blinks");
  numOfBlinks = 8;
  delay(1000);
}

void handle_500msDelay()
{
  server.send(200, "text/html", getpage());
  Serial.println("500ms delay");
  delayMS = 500;
  delay(1000);
}


void handle_1000msDelay()
{
  server.send(200, "text/html", getpage());
  Serial.println("1000ms delay");
  delayMS = 1000;
  delay(1000);
}


void handle_1500msDelay()
{
  server.send(200, "text/html", getpage());
  Serial.println("1500ms delay");
  delayMS = 1500;
  delay(1000);
}


void handle_2000msDelay()
{
  server.send(200, "text/html", getpage());
  Serial.println("2000ms delay");
  delayMS = 2000;
  delay(1000);
}