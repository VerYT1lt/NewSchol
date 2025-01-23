
import requests
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import F
import asyncio


BOT_TOKEN = '7766088929:AAGFdwHr8PjRcweVl_4MZV-ySSl58m9cY1Q'


IMAGE_API_URL = 'https://serpapi.com/search?engine=google_images'


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Привет! Отправь мне описание изображения, и я сгенерирую его для тебя!")


@dp.message(F.text)
async def generate_image(message: Message):
    prompt = message.text
    await message.answer("Генерирую изображение, подожди немного...")

    try:

        response = requests.post(IMAGE_API_URL, json={"prompt": prompt})


        if response.status_code == 200:
            data = response.json()
            image_url = data.get('image_url')

            if image_url:

                await bot.send_photo(chat_id=message.chat.id, photo=image_url)
            else:
                await message.answer("Не удалось получить изображение.")
        else:
            await message.answer("Ошибка при запросе к API.")
    except Exception as e:
        await message.answer(f"Произошла ошибка: {e}")


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())