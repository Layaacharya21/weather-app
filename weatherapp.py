import requests
import tkinter as tk 
from tkinter import messagebox
import ttkbootstrap

def get_weather(city):
    api_key="26fca9c7080e04c23ed93706808acaa0"
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    request=requests.get(url)

    if request.status_code==404:
        messagebox.showerror("Error, City not found")
        return None
    weather=request.json()
    icon_id=weather['weather'][0]['icon']
    temperature=weather['main']['temp'] - 273.15
    description=weather['weather'][0]['description']
    city=weather['name']
    country=weather['sys']['country']

    return (temperature,description,city,country)



def search():
    city=city_entry.get()
    result=get_weather(city)
    if result is None:
        return
    temperature,description,city,country=result
    location_label.configure(text=f"{city},{country}")
    temp.configure(text=f"Temperature: {temperature:.2f} C")
    description_label.configure(text=f"Description: {description}")

root=tk.Tk()
root.title("Weather App")
root.geometry("400x400")

city_entry=ttkbootstrap.Entry(root, font="Helvetica,18")
city_entry.pack(pady=10)

search_button=ttkbootstrap.Button(root,text="Search",command=search,bootstyle="warning")
search_button.pack(pady=10)

location_label=tk.Label(root,font="Helvetica,20")
location_label.pack(pady=20)

icon_label=tk.Label(root)
icon_label.pack()

temp=tk.Label(root,font="Helvetica,20")
temp.pack()

description_label=tk.Label(root,font="Helvetica,20")
description_label.pack()

root.mainloop()
