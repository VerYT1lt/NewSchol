

#Задача 1: Асинхронное программирование
# import aiohttp
# import asyncio
#
# urls = [
#     "https://filesamples.com/samples/document/txt/sample3.txt",
#     "https://filesamples.com/samples/document/txt/sample2.txt",
#     "https://filesamples.com/samples/document/txt/sample1.txt"
# ]
#
#
# async def download_file(session, url):
#     filename = url.split("/")[-1]
#     async with session.get(url) as response:
#         with open(filename, 'wb') as f:
#             f.write(await response.read())
#         print(f'{filename} загружен')
#
#
# async def download_all_files(urls):
#     async with aiohttp.ClientSession() as session:
#         tasks = [download_file(session, url) for url in urls]
#         await asyncio.gather(*tasks)


#Задача 2: Асинхронная обработка задач
# async def calculate_square(number):
#     await asyncio.sleep(1)
#     square = number ** 2
#     print(f"Квадрат числа {number} равен {square}")
#     return square
#
#
# async def process_numbers(numbers):
#     tasks = [calculate_square(number) for number in numbers]
#     results = await asyncio.gather(*tasks)
#     return results
#
#
# numbers = [1, 2, 3, 4, 5]
# asyncio.run(process_numbers(numbers))

#Задача 3: Синхронизация потоков
import threading

counter = 0
lock = threading.Lock()


def increment_counter():
    global counter
    for _ in range(1000):
        with lock:
            counter += 1


threads = []
for i in range(10):
    thread = threading.Thread(target=increment_counter)
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()

print("Значение общего счетчика:", counter)