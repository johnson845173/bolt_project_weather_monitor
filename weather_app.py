from tkinter import messagebox
from db_conn import engine,processQuery
from tkinter import *
from threading import Thread
from sensor import Sensor
import pandas as pd
import telegram 
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))
sensors = Sensor()
class Weather:

    def upload_button(self):
        th = Thread(target=sensors.get_and_upload)
        th.start()
        if sensors.push_value:
            self.upload_status['text'] = "Push Successful"
            self.upload_status['bg'] = self.green
            messagebox.showinfo(title="Upload status",message="Data Successfully Pushed")
        else:
            self.upload_status['text'] = "Push Failed"
            self.upload_status['bg'] = self.red
            messagebox.showerror(title="Upload status",message="Data Push Fail")

    def send_telegram_msg(self):
        tele_respone = telegram.send_msg(sensors.read_sensor())
        if tele_respone:
            self.send_status['text'] = "Message sent"
            self.send_status['bg'] = self.green
            messagebox.showinfo(title="Message status",message="Message sent successfully")
        else:
            self.send_status['text'] = "Message not sent"
            self.send_status['bg'] = self.red
            messagebox.showerror(title="Message status",message="Failed to send message")
    
    def generate_excel(self):
        file_name = self.file_name.get()
        if(len(file_name)>0):
            outputDF = pd.DataFrame(columns=['Time \nYear-Month-day Hour:Min:sec', 'Temprature', 'Humidity', 'Light Intensity', 'Air Quality'])
            data = sensors.get_table_data()
            for each_entry in data.index:
                row_data = [data['record_created'][each_entry],data['temprature'][each_entry],data['humidity'][each_entry],data['light_intensity'][each_entry],data['smoke'][each_entry]]
                outputDF.loc[len(outputDF)] = row_data
            
            outputDF.to_excel(f"{file_name}.xlsx")
            self.excel_status['text'] = "Excel Generated"
            self.excel_status['bg'] = self.green
            messagebox.showinfo(title="Success", message="File Generated Successfully")
        else:
            messagebox.showerror(title="Error", message="Please Enter File Name")
            self.excel_status['text'] = "Generation Failed"
            self.excel_status['bg'] = self.red
       

    def __init__(self) -> None:
        sensors.intial_values()
        self.colour = '#ffddcc'
        self.red    = '#ff704d'
        self.green  = '#33ff33'
        self.yellow = '#ffff1a'
        self.sky_blue = '#66e0ff'
        self.light_green = '#9fff80'
        self.dark_yellow = '#ffb380'
        self.font_style = ('Arial',24)
        self.side_style = ('Arial',14)
        self.new_style = ('Arial',18)
        window = Tk()
        self.file_name = StringVar()
        window.geometry("900x600") #width*hhieght
        window.config(bg=self.sky_blue)
        window.resizable(False,False)

        #=============================================Frame Section========================================================================

        title_frame = Frame(master = window, bg=self.green)
        title_frame.grid(row=0, column=0,columnspan=3)

        main_frame = Frame(master = window, bg=self.red)
        main_frame.grid(row=1, column=1)

        side_frame = Frame(master = window, bg=self.yellow)
        side_frame.grid(row=1, column=0,sticky=(N,W))

        data_frame = Frame(master = window, bg=self.yellow)
        data_frame.grid(row=1, column=2,sticky=(E,N))

       
        #==================================================Title Page==================================================================
        
        heading = Label(master=title_frame, text="Weather Station", font = self.font_style,width=47, bg=self.green)
        heading.grid(row = 0, column = 0)

        #====================================================Control Panel===================================================================
        
        Label(master = data_frame,text ="Data Panel",font=self.new_style, bg=self.dark_yellow).grid(row=0,column=0,columnspan=2, padx = 15, pady = 10)
        
        upload_button = Button(master= data_frame, text="Upload Data", command=self.upload_button, width=15)
        upload_button.grid(row = 1, column = 0, pady=10, padx = 10)
        self.upload_status = Label(master= data_frame, text=" Upload Status", width=15)
        self.upload_status.grid(row = 1, column = 1, pady=10, padx = 10)

        send_button = Button(master= data_frame, text="Send Message", command=self.send_telegram_msg, width=15)
        send_button.grid(row = 2, column = 0, pady=10, padx = 10)
        self.send_status = Label(master= data_frame, text=" Message Status", width=15)
        self.send_status.grid(row = 2, column = 1, pady=10, padx = 10)

        gen_excel = Button(master= data_frame, text="Generate Excel", command=self.generate_excel, width=15)
        gen_excel.grid(row = 3, column = 0, pady=10, padx = 10)
        self.entry = Entry(master= data_frame, textvariable=self.file_name)
        self.entry.grid(row = 3, column = 1, pady=10, padx = 10)
        self.excel_status = Label(master= data_frame, text=" Excel Status", width=25)
        self.excel_status.grid(row = 4, column = 0,columnspan=2, pady=10, padx = 10)

        #====================================================Side Frame=======================================================================
        
        Label(master = side_frame,text ="Current Weather",font=self.new_style, bg=self.dark_yellow,width=19).grid(row=0,column=0,columnspan=2, padx = 5, pady = 5)

        Label(master = side_frame,text ="Temprature:",font=self.side_style, bg=self.yellow).grid(row=1,column=0, sticky = E, padx = 5, pady = 5)
        self.cur_temp = Label(master = side_frame,text =f"{sensors.temperature}°C", bg=self.yellow)
        self.cur_temp.grid(row=1,column=1, padx = 5, pady = 5)

        Label(master = side_frame,text ="Humidity:",font=self.side_style, bg=self.yellow).grid(row=2,column=0, sticky = E, padx = 5, pady = 5)
        self.cur_humidity = Label(master = side_frame,text =sensors.humidity, bg=self.yellow)
        self.cur_humidity.grid(row=2,column=1, padx = 5, pady = 5)

        Label(master = side_frame,text ="Light Intensity:",font=self.side_style, bg=self.yellow).grid(row=3,column=0, sticky = E, padx = 5, pady = 5)
        self.cur_light = Label(master = side_frame,text =sensors.light, bg=self.yellow)
        self.cur_light.grid(row=3,column=1, padx = 5, pady = 5)

        Label(master = side_frame,text ="Air Quality:",font=self.side_style, bg=self.yellow).grid(row=4,column=0, sticky = E, padx = 5, pady = 5)
        self.cur_air = Label(master = side_frame,text =sensors.smoke, bg=self.yellow)
        self.cur_air.grid(row=4,column=1, padx = 5, pady = 5)

    
        
        window.mainloop()

if __name__ == "__main__":
    app = Weather()    

