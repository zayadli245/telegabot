import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import config

logging.basicConfig(level=logging.INFO)

#Замените TOKEN на ваш токен бота
API_TOKEN = config.token

#Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

#Обработчик команды /start
@dp.message(Command("start"))
async def send_welcome(message: types.Message):

    await message.answer("Привет! Я эхобот на aiogram 3. Отправь мне сообщение, и я его повторю.")

#Обработчик команды /start
@dp.message(Command("info"))
async def echo(message: types.Message):

    await message.answer("Данный бот предоставляет простую функцию: получить дублирование своего ответа")

#Обработчик команды /start
@dp.message(Command("user"))
async def echo(message: types.Message):

    await message.answer("Вы пользователь №1. Спасибо вам!")

#Обработчик всех сообщений
@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)

#Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())