import telebot
import requests
import os
from dotenv.main import load_dotenv

load_dotenv()
BotToken = os.environ['WeatherBot']

# Function to fetch weather
def fetchWeather(city):
    try:
        url = "https://weather-by-api-ninjas.p.rapidapi.com/v1/weather"

        querystring = {"city": city}

        headers = {
            "X-RapidAPI-Key": os.environ['WeatherAPIKey'],
            "X-RapidAPI-Host": "weather-by-api-ninjas.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        return response.json()
    except:
        return "An unexpected error occured or Check city name and your internet connection"

# query = fetchWeather('Delhi')
# print(query['temp'])

# Creating instance of bot
bot = telebot.TeleBot(BotToken)

#  Creating message handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(
        message, "Hey I am a bot that can tell weather. Give me a city name")

# Bot will give weather status
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    try:
        query = fetchWeather(message.text)

        temp = query['temp']
        cloud_pct = query['cloud_pct']
        feels_like = query['feels_like']
        humidity = query['humidity']
        min_temp = query['min_temp']
        max_temp = query['max_temp']
        wind_speed = query['wind_speed']
        wind_degrees = query['wind_degrees']
    
        result = f'''TODAY's weather of {message.text}
1. Temperature -> {temp}°C
2. Cloud PCT -> {cloud_pct}
3. Feels Like -> {feels_like}°C
4. Humidity -> {humidity}
5. Minimum Temperature -> {min_temp}°C
6. Maximum Temperature -> {max_temp}°C
7. Wind Speed -> {wind_speed}m/s
8. Wind Degrees -> {wind_degrees}'''

        bot.reply_to(message, result)
    except:
        bot.reply_to(message, "An unexpected error occured or Check city name and your internet connection")

bot.infinity_polling()