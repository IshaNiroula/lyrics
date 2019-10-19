'''
import lyricwikia

a = input("Enter the name of Singer: ")
b= input("Enter the name of Song: ")

lyrics = lyricwikia.get_lyrics(a,b)

print("\n",lyrics)



import requests
api_key='a02d44d26449cca42e610f5c7239c6f6'
base_url = "http://api.openweathermap.org/data/2.5/weather?"
appid = {api_key}
city_name = "Sydney"
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
#response = requests.get(complete_url)
#x = response.json()
print(requests.get(complete_url).json())



from tkinter import *
master = Tk()

scrollbar = Scrollbar(master)

scrollbar.pack(side = RIGHT,fill = Y)

listbox = Listbox(master,yscrollcommand = scrollbar.set)
for i in range(1000):
    listbox.insert(END , 'APPLE')
listbox.pack(side = LEFT,fill = BOTH)

scrollbar.config(command = listbox.yview)

mainloop()

from tkinter import *

root = Tk()
S = Scrollbar(root)
T = Text(root, height=4, width=50)
S.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
quote = """HAMLET: To be, or not to be--that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune
Or to take arms against a sea of troubles
And by opposing end them. To die, to sleep--
No more--and by a sleep to say we end
The heartache, and the thousand natural shocks
That flesh is heir to. 'Tis a consummation
Devoutly to be wished."""
T.insert(END, quote)
mainloop(  )

'''

import requests, json
api_key = "Your_API_Key"

base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter city name : ")

complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(complete_url)

x = response.json()

if x["cod"] != "404":

    y = x['main']

    current_temperature = y["temp"]

    current_pressure = y["pressure"]

    current_humidiy = y["humidity"]

    z = x["weather"]


    weather_description = z[0]["description"]

    print(" Temperature (in kelvin unit) = " +
          str(current_temperature) +
          "\n atmospheric pressure (in hPa unit) = " +
          str(current_pressure) +
          "\n humidity (in percentage) = " +
          str(current_humidiy) +
          "\n description = " +
          str(weather_description))

else:
    print(" City Not Found ")
