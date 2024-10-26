
import psycopg2
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from contextlib import closing


conn = psycopg2.connect(
    dbname="persondb",
    user="postgres",
    password="user",
    host="localhost"
)


BOT_TOKEN = '7766088929'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("add"))
async def add_person(message: Message):
    await message.answer("Введите имя, фамилию и возраст через запятую:")

    @dp.message(F.text)
    async def process_add_command(new_message: Message):
        try:
            data = new_message.text.split(',')
            first_name = data[0].strip()
            last_name = data[1].strip()
            age = int(data[2].strip())

            with closing(conn.cursor()) as cursor:
                cursor.execute(
                    'INSERT INTO person (first_name, last_name, age) VALUES (%s, %s, %s)',
                    (first_name, last_name, age)
                )
                conn.commit()

            await new_message.answer(f'{first_name} {last_name} добавлен в базу данных.')
        except Exception as e:
            await new_message.answer("Ошибка при добавлении человека.")


@dp.message(Command("show"))
async def show_people(message: Message):
    with closing(conn.cursor()) as cursor:
        cursor.execute('SELECT * FROM person')
        people = cursor.fetchall()

        if not people:
            await message.answer('База данных пуста.')
        else:
            response = '\n'.join([f"Имя: {person[1]}, Фамилия: {person[2]}, Возраст: {person[3]}" for person in people])
            await message.answer(response)


@dp.message(Command("delete"))
async def delete_person(message: Message):
    await message.answer("Введите ID человека для удаления:")

    @dp.message(F.text)
    async def process_delete_command(new_message: Message):
        try:
            person_id = int(new_message.text.strip())
            with closing(conn.cursor()) as cursor:
                cursor.execute('DELETE FROM person WHERE id_person = %s', (person_id,))
                conn.commit()
            await new_message.answer(f'Человек с ID {person_id} удален из базы данных.')
        except Exception as e:
            await new_message.answer("Ошибка при удалении человека.")




dp.start_polling(bot)
