from pyexpat.errors import messages

API_KEY = '649491f17a6529e06b055842a56409f2'

import asyncio
import logging

import requests
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

bot = Bot(token="7601465224:AAEsFJxu1WZOQbKqtifjQl1MxgdEOJM9fz8")
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)


def reyly_button():
    buttons = [
        [KeyboardButton(text="Ob-havo malumotlari")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)


def weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        latitude = data['coord']['lat']
        langitude = data['coord']['lon']
        namkil = data['main']['humidity']
        temprature = data ['main']['temp'] - 273
        city_name  = data ['name']
        country = data['sys']['country']
        weather = data['weather'][0]['main']
        wind_speed = data['wind']['speed']

        text = f"{city_name}({country}) \n issiqlik darajasi: {temprature} \n OB-Havo holat: {weather} \n Namlik: {namkil} \n Shamol tezligi: {wind_speed} "
        return text, langitude, latitude



@dp.message(Command('start'))
async def start_button(message: Message):
    print(message.from_user.id)
    await message.answer(text="Assalomu alaykum", reply_markup= reyly_button())

@dp.message(lambda message: message.text == "Ob-havo malumotlari")
async def weather_data1(message: Message):
    await message.answer(text="Shaxar nomini kiriitng")
@dp.message()
async def result(message: Message):
    city = message.text
    text = weather_data(city)
    if not text:
        await message.answer(text="Bunday shaxar nomi topilmadi")

    await bot.send_location(chat_id=message.chat.id,
    latitude=text[1],
    longitude=text[2]
    )
    await message.answer(text=text[0])


async def main():
    print("WORKING")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
