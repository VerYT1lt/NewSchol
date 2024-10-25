import asyncio
import random
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

BOT_TOKEN = '7766088929'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_game(message: Message):
    await message.answer("Привет! Добро пожаловать в игру 'Кости'.\n"
                         "Напиши /roll, чтобы бросить кости и посмотреть, кто победит!")


@dp.message(Command("roll"))
async def roll_dice(message: Message):
    player_roll = random.randint(1, 6)
    bot_roll = random.randint(1, 6)

    result = f"🎲 Вы бросили: {player_roll}\n🤖 Бот бросил: {bot_roll}\n\n"

    if player_roll > bot_roll:
        result += "🎉 Вы победили!"
    elif player_roll < bot_roll:
        result += "😔 Бот победил!"
    else:
        result += "🤝 Ничья!"

    await message.answer(result)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
