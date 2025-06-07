import asyncio
from aiogram import Bot, Dispatcher, types

API_TOKEN = "YOUR_BOT_TOKEN"  # Замени на токен своего бота

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message()
async def echo_handler(message: types.Message):
    await message.answer(f"Привет, ты написал: {message.text}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
