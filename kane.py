
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
#30 июня
#Смотреть выше(то же самое )

#3 июля
#1
# class Person:
#     pass
#
# id_1 = Person()
#
# setattr(id_1, "name", "Vasya")
#
# setattr(id_1, "name", "Masha")
#
# print(id_1.name)
# #2
# class Person:
#     setup = ['имя ', 'Годиков', 'работа', 'Учться ли?']
#
# id_1 = Person()
# for attribute in id_1.setup:
#     value = input(f"Введите значение для {attribute}: ")
#     setattr(id_1, attribute, value)
#
#
# for attribute in id_1.setup:
#     print(f"{attribute}: {getattr(id_1, attribute)}")
#3
# class Person:
#     pass
#
#
# id_1 = Person()
#
#
# setattr(id_1, "dance", "Hip Hop")
# setattr(id_1, "draw", "Sketching")
# setattr(id_1, "sing", "Opera")
#
#
# attributes = ["dance", "draw", "sing"]
#
#
# for attr in attributes:
#     print(getattr(id_1, attr))
#6 июля
#1
# class Homer:
#     def __init__(self, name):
#         self.name = name
#
# class Daughter(Homer):
#     pass
#
# daughter1 = Daughter("Lisa")
#
#
# print(daughter1.name)
#2
# class Shape:
#     def calculate_area(self):
#        pass
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def calculate_area(self):
#         return self.width * self.height
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def calculate_area(self):
#         import math
#         return math.pi * (self.radius ** 2)
#
# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
#
#     def calculate_area(self):
#         return 0.5 * self.base * self.height
#
#
# rectangle = Rectangle(5, 10)
# circle = Circle(7)
# triangle = Triangle(6, 8)
#
# print(rectangle.calculate_area())
# print(circle.calculate_area())
# print(triangle.calculate_area())
#3
# class Animal:
#     def make_sound(self):
#         pass
#
# class Dog(Animal):
#     def make_sound(self):
#         return "Woof"
#
# class Cat(Animal):
#     def make_sound(self):
#         return "Meow"
#
# class Bird(Animal):
#     def make_sound(self):
#         return "Tweet"
#
#
# dog = Dog()
# cat = Cat()
# bird = Bird()
#
# print(dog.make_sound())
# print(cat.make_sound())
# print(bird.make_sound())