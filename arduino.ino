#include <DHT.h>
#include <LiquidCrystal.h>

#define DHTTYPE DHT11
#define DHTPIN 3

String readdata;
int RS = 4,E = 5,D4 = 9,D5 = 10,D6 = 11,D7 = 12;   //Intialize the pins of LCD

LiquidCrystal lcd(RS,E,D4,D5,D6,D7);  //Configure the LCD Pins

DHT dht(DHTPIN,DHTTYPE);

void setup()
{
  
 Serial.begin(9600);        //Begin the Serial Communcation at Baud Rate of 9600
 lcd.begin(16,2);           //Intialize the LCD of 2 rows and 16 columns
 dht.begin();               //Intialize the DHT Sensor

 //Declare the pinmode for all the sensors
 pinMode(A5, INPUT);
 pinMode(8,INPUT);
 pinMode(9,OUTPUT);
//https://cloud.boltiot.com/remote/487b1d2a-e884-4e88-b88c-526aa4bc7721/serialWrite?data=RD&deviceName=BOLT14854650
}
void loop(){
  
  //Reading all the Sensor values
  float smoke = analogRead(A5);
  String intensity = brightness(digitalRead(2));
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();
  
  String inputmessage = Serial.readString();
  
  if(inputmessage.compareTo("RD") == 0)
  {
    String data = "smoke:"+String(smoke)+" light:"+String(digitalRead(2))+" humidity:"+String(humidity)+" temperature:"+String(temperature);
    Serial.print(data);     
  }
 
  //Displaying the Values of various Sensors on the LCD display
  showdata("Temprature  ",String(temperature),"\337C" );
  showdata("Humidity  ",String(humidity),"%");
  showdata("Intensity  ",intensity," ");
  showdata("Smoke  ",String(smoke),"ppm"); 
}

//Creating a fuction to dsiplay the values on to the lcd by taking 3 parameters 
void showdata(String sensor_name, String value, String SIunit)
{
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print(sensor_name);
  lcd.setCursor(0,1);
  lcd.print(value);
  lcd.print(SIunit);
}

// This Function reads the Value Of ldr and depending on the intensity determines wether it is day or night
String brightness(int intensity_value)
{
 if(intensity_value == 0) return "It's bright outside";
  else return "It's dark outside";
}