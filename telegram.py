import requests

import conf

def send_msg(val):
    try :
        weather_info = val.split(" ")

        smoke = weather_info[0].split(":")
        humidity = weather_info[2].split(":")
        temperature = weather_info[3].split(":")
        light = weather_info[1].split(":")

        if light == "1":
            weather = "It's bright outside"
        else:
            weather = "It's dark outside"

        message = f"hello the temperature is {temperature[1]}°C\nhumidity is {humidity[1]}%" \
                f"\n{weather}\nCo concentration is{smoke[1]}ppm"

        teleurl = "https://api.telegram.org/"+conf.telegram_bot_id+"/sendMessage"
        data = {
            "chat_id": conf.telegram_chat_id,
            "text": message
        }
        requests.post(teleurl, params=data)
        return True
        
    except Exception as e:
        print(e)
        return False
