import conf
import json
import requests
from db_conn import engine,processQuery
from datetime import datetime

class Sensor:
    def request_data(self):
        respone = requests.get(conf.request_url)

    def read_sensor(self):
        response = requests.request("GET", conf.geturl)
        response = json.loads(response.text)
        val = response["value"]
        return val

    def convert_to_dict(self, received_string):
            mydict = dict((sensor_name.strip(), sensor_value.strip()) for sensor_name,sensor_value in 
                        (item.split(':') for item in received_string.split(' ')))
            return mydict

    def get_values_from_dict(self, dictionary):
        self.temperature = dictionary['temperature']
        self.humidity = dictionary['humidity']
        self.smoke = dictionary['smoke']
        self.light = dictionary['light']

    def push_data(self):
        creation_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            query = f"INSERT INTO public.weather_data(\
                temprature, humidity, smoke, light_intensity, status, record_created)\
                VALUES ({self.temperature}, {self.humidity}, {self.smoke}, {self.light}, 0, '{creation_time}');"
            engine.execute(query)
        except Exception as e:
            print(e)
            self.push_value = False
        else:
            self.push_value = True

    def update_status(self):
        query = "UPDATE public.weather_data SET status= 1 WHERE status= 0"
        engine.execute(query)

    def get_and_upload(self):
        self.update_status()
        recived_data = self.read_sensor()
        mydict = self.convert_to_dict(recived_data)
        self.get_values_from_dict(mydict)
        self.push_data()
    
    def get_table_data(self):
        query = "SELECT record_created,temprature, humidity, light_intensity, smoke FROM public.weather_data;"
        data = processQuery(query)
        return data
    
    def intial_values(self):
        recived_data = self.read_sensor()
        mydict = self.convert_to_dict(recived_data)
        self.get_values_from_dict(mydict)