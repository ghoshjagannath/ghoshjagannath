from gtts import gTTS 
from dotenv import load_dotenv
import os,playsound,requests

import pyttsx3





#loading local env file to get api key for weatherapi  
load_dotenv("C:/Users/ghosh/AppData/Local/Programs/Python/Python39/Weather_project/.env")

# print(type(os.getenv('api_key')))



count=0
def voice(data_of_temp):
    global count
    string=f'the temperature is {data_of_temp}'
    
    myobj=gTTS(string,lang='en',slow=False)
    file_name='media_dj.mp3'
    myobj.save(file_name)
    playsound.playsound(file_name, True)
    os.remove(file_name)
    count+=1




# here is the problem 

#this function collection city temparture data in celcius  unit.
#for tkinter  if user click celcius radio button he will call this function 
def temperature_of_place_c(name):
    try:
        url=f"https://api.weatherapi.com/v1/current.json?key={os.getenv('api_key')}&q={name}&aqi=yes"
        res=requests.get(url).json()
        data=res['current']['temp_c']
        voice(data)
    except KeyError:
        string_data="for Your given data is not correct, Kindly check once more"
        voice(string_data)    


#additional function is made to get value of temparature in farenheit of a particular city 
#for tkinter  if user click farenheit radio button he will call this function 

def temperature_of_place_f(name):
    try:
        url=f"https://api.weatherapi.com/v1/current.json?key={os.getenv('api_key')}&q={name}&aqi=yes"
        res=requests.get(url).json()
        data=res['current']['temp_f']
        voice(data)
    except KeyError:
        string_data="for Your given data is not correct, Kindly check once more"
        voice(string_data)    




lis=['howrah','delhi','noida','London']


for name in lis:
    temperature_of_place_f(name)