import tkinter as tk
from tkinter import messagebox
import requests

#Function to get weather data
def get_weather():

    #get city name from user
    city = city_entry.get()

    if city == "":
        messagebox.showwarning("Input Error", "Please enter a city name ")
        return

    #Open weather app API url with API key
    api_key = "0453de2eb6e73d17517457aae7d14926"
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    #make a request to Openweather app
    response = requests.get(base_url)

    #check if the request was successful
    if response.status_code == 200:
        data = response.json()

        #Extraxt the weather data
        main = data['main']
        weather = data['weather'][0]
        temperature = main['temp']
        description = weather['description']
        pressure = main['pressure']
        humidity = main['humidity']

        # Display the weather information
        result_label.config(text=f"Temperature: {temperature}°C\n"
                                 f"Description: {description.capitalize()}\n"
                                 f"Pressure: {pressure} hPa\n"
                                 f"Humidity: {humidity}%")
    else:
        #If city not found or other error
        messagebox.showerror("Input error", "City not found or invalid API key")

#set up tkiter window
root = tk.Tk()
title = root.title("Weather APP")

#set the window size
root.geometry("400x300")

#Add city entry label
city_label = tk.Label(text= "Input a city to check the weather", font=("Helvetica", 14))
city_label.pack()

#Add city entry
city_entry = tk.Entry(root, font=("Helvetica", 14))
city_entry.pack()

#Add get weather btn
get_weather_btn = tk.Button(root, text= "Get Weather", font=("Helvetica", 14), command=get_weather)
get_weather_btn.pack()

#Result label
result_label = tk.Label(root, text="", font=("Helvetica", 12), justify=tk.LEFT)
result_label.pack()

#run program
root.mainloop()

