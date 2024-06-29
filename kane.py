
#22 июня дз
# class Car:
#     def __init__(self):
#         self.model = ""
#         self.year = 0
#         self.manufacturer = ""
#         self.engine_capacity = 0.0
#         self.color = ""
#         self.price = 0.0
#
#     def input_data(self):
#         self.model = input("Что за модель машины: ")
#         self.year = input("Укажите год выпуска: ")
#         self.manufacturer = input("Введите производителя: ")
#         self.engine_capacity = float(input("Введите мощность двигателя: "))
#         self.color = input("Цвет: ")
#         self.price = float(input("Сюда обычно входит кредит хммм??: "))
#
#     def output_data(self):
#         print("Car Model:", self.model)
#         print("Year of Manufacture:", self.year)
#         print("Manufacturer:", self.manufacturer)
#         print("Engine Capacity:", self.engine_capacity)
#         print("Color:", self.color)
#         print("Price:", self.price)
#
#     def get_model(self):
#         return self.model
#
#     def get_year(self):
#         return self.year
#
#     def get_manufacturer(self):
#         return self.manufacturer
#
#     def get_engine_capacity(self):
#         return self.engine_capacity
#
#     def get_color(self):
#         return self.color
#
#     def get_price(self):
#         return self.price
#
#
# class Book:
#     def __init__(self):
#         self.title = ""
#         self.year = 0
#         self.publisher = ""
#         self.genre = ""
#         self.author = ""
#         self.price = 0.0
#
#     def input_data(self):
#         self.title = input("Введите название книги: ")
#         self.year = input("Укажите год публикации: ")
#         self.publisher = input("Введите имя издателя: ")
#         self.genre = input("Жанр: ")
#         self.author = input("Его автор: ")
#         self.price = float(input("Цена книги: "))
#
#     def output_data(self):
#         print("Book Title:", self.title)
#         print("Year of Publication:", self.year)
#         print("Publisher:", self.publisher)
#         print("Genre:", self.genre)
#         print("Author:", self.author)
#         print("Price:", self.price)
#
#     def get_title(self):
#         return self.title
#
#     def get_year(self):
#         return self.year
#
#     def get_publisher(self):
#         return self.publisher
#
#     def get_genre(self):
#         return self.genre
#
#     def get_author(self):
#         return self.author
#
#     def get_price(self):
#         return self.price
#
#
# class Stadium:
#     def __init__(self):
#         self.name = ""
#         self.opening_date = ""
#         self.country = ""
#         self.city = ""
#         self.capacity = 0
#
#     def input_data(self):
#         self.name = input("Что за стадион: ")
#         self.opening_date = input("Введите дату открытия: ")
#         self.country = input("Введите страну: ")
#         self.city = input("Введите город: ")
#         self.capacity = int(input("Введите вместимость стадиона: "))
#
#     def output_data(self):
#         print("Stadium Name:", self.name)
#         print("Opening Date:", self.opening_date)
#         print("Country:", self.country)
#         print("City:", self.city)
#         print("Capacity:", self.capacity)
#
#     def get_name(self):
#         return self.name
#
#     def get_opening_date(self):
#         return self.opening_date
#
#     def get_country(self):
#         return self.country
#
#     def get_city(self):
#         return self.city
#
#     def get_capacity(self):
#         return self.capacity
# car = Car()
# car.input_data()
# car.output_data()
#
#
# book = Book()
# book.input_data()
# book.output_data()
#
#
# stadium = Stadium()
# stadium.input_data()
# stadium.output_data()
# 26 июня

# class TriangleChecker:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def is_triangle(self):
#         if not all(isinstance(x, (int, float)) for x in [self.a, self.b, self.c]):
#             return "Нужно вводить только числа!"
#         if any(x <= 0 for x in [self.a, self.b, self.c]):
#             return "С отрицательными числами ничего не выйдет!"
#         if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
#             return "Ура, можно построить треугольник!"
#         else:
#             return "Жаль, но из этого треугольник не сделать."

# Пример использования:
# checker = TriangleChecker(3, 4, 5)
# print(checker.is_triangle())
#
# checker = TriangleChecker(1, 1, 2)
# print(checker.is_triangle())
#
# checker = TriangleChecker(3, -4, 5)
# print(checker.is_triangle())
#
# checker = TriangleChecker(3, '4', 5)
# print(checker.is_triangle())



# class KgToPounds:
#     def __init__(self, kg):
#         self._kg = kg
#
#     @property
#     def kg(self):
#         return self._kg
#
#     @kg.setter
#     def kg(self, value):
#         if isinstance(value, (int, float)):
#             self._kg = value
#         else:
#             raise ValueError("Килограммы должны быть числом")
#
#     def to_pounds(self):
#         return self._kg * 2.20462
#
# converter = KgToPounds(10)
# print(converter.to_pounds())
#
# converter.kg = 20
# print(converter.kg)
# print(converter.to_pounds())