import telebot
import requests
import json
import datetime


token='5282559456:AAHDWHBZVKsqZMSwxagnMjBsdR-g-uC9vM4'
bot = telebot.TeleBot(token=token)

@bot.message_handler(commands=['start'])
def send_start(message):
    bot.send_message(message.chat.id, "Привет, Я Погодагоп-бот напишите страну")

@bot.message_handler(content_types='text')
def send_data(message):
    API_key = 'ca47be775bcdce04caa140c563a84b6d'
    city = message.text.title()
    API = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_key}'
    data = requests.get(API).json()
    coord = data['main']['temp']
    flike = data['main']['feels_like']
    min_temp = data['main']['temp_min']
    max_temp = data['main']['temp_max']
    bot.send_message(message.chat.id, f"Температура:{coord} \n Ощушается как:{flike}")
        
        
print('Бот работает...')
bot.infinity_polling()