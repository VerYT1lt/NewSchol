# 22 июня дз
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
# 30 июня
# Смотреть выше(то же самое )

# 3 июля
# 1
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
# 3
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
# 6 июля
# 1
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
# 2
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
# 3
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
# 10 июля
# 1
# class Bank:
#     def __init__(self, client_name, card_number, balance):
#         self.__client_name = client_name
#         self.__card_number = card_number
#         self.__balance = balance
#
#     def print_balance(self):
#         print(f"Balance: {self.__balance}")
#
#     def change_balance(self, money):
#         self.__balance += money
# bank_account = Bank("Alice", "1234-5678-9012-3456", 1000)
# bank_account.print_balance()
# bank_account.change_balance(200)
# bank_account.print_balance()
# 2
# class Bank:
#     def __init__(self, client_name, card_number, balance):
#         self.__client_name = client_name
#         self.__card_number = card_number
#         self.__balance = balance
#
#     def print_balance(self):
#         print(f"Balance: {self.__balance}")
#
#     def change_balance(self, money):
#         self.__balance += money
#
#     @property
#     def balance(self):
#         return self.__balance
#
#     @balance.setter
#     def balance(self, new_balance):
#         self.__balance = new_balance
#
#     @balance.deleter
#     def balance(self):
#         self.__balance = 0
#
#
# bank_account = Bank("Masha", "9876-5432-1098-7654", 1500)
# print(bank_account.balance)
# bank_account.balance = 2000
# print(bank_account.balance)
# del bank_account.balance
# print(bank_account.balance)
# 13 июля
# from figures import circle_area, triangle_perimeter, square_area
#
# print(circle_area(10))  # Площадь окружности с радиусом 10
# print(triangle_perimeter())  # Периметр треугольника со сторонами по умолчанию
# print(square_area(5))  # Площадь квадрата со стороной 5
# 18 Июля
# import random
# import pygame, sys
#
# pygame.init()
# screen = pygame.display.set_mode((500, 500))
# clock = pygame.time.Clock()
#
# PARTICLE_EVENT = pygame.USEREVENT + 1
# pygame.time.set_timer(PARTICLE_EVENT, millis=1)
# nyan_surface = pygame.image.load('images/Anime.gif').convert_alpha()
#
#
#
#
#
# class ParticlePrinciple:
#     def __init__(self):
#         self.particles = []
#         self.size = 8
#
#
#     def emit(self):
#         if self.particles:
#             self.delete_particles()
#         # for particle in self.particles:
#         #     particle[0][1] += particle[2][0]
#         #     particle[0][0] += particle[2][1]
#         #     particle[1] -= 0.2
#         #     pygame.draw.circle(screen, pygame.Color('White'), particle[0], int(particle[1]))
#         for particle in self.particles:
#             particle[0].x -= 2
#             pygame.draw.rect(screen, particle[1], particle[0])
#             pygame.draw.rect(screen, particle[1], particle[0])
#         self.draw_nyancat()
#
#
#
#
#
#     def add_particles(self,offset, color):
#         # pos_x = pygame.mouse.get_pos()[0]
#         # pos_y = pygame.mouse.get_pos()[1]
#         # radius = 10
#         # direction_x = random.randint(-3, 3)
#         # direction_y = random.randint(-3, 3)
#         # particle_circle = [[pos_x, pos_y], radius, [direction_x, direction_y]]
#         # self.particles.append(particle_circle)
#         pos_x = pygame.mouse.get_pos()[0]
#         pos_y = pygame.mouse.get_pos()[1] + offset
#         particle_rect = pygame.Rect(pos_x - self.size / 2, pos_y - self.size / 2,self.size, self.size)
#         self.particles.append((particle_rect, color))
#
#
#
#
#     def delete_particles(self):
#         # particles_copy = [particle for particle in self.particles if particle[1] > 0]
#         # self.particles = particles_copy
#         particles_copy = [particle for particle in self.particles if particle[0].x > 0]
#         self.particles = particles_copy
#     def draw_nyancat(self):
#         nyan_rect = nyan_surface.get_rect(center=pygame.mouse.get_pos())
#         screen.blit(nyan_surface, nyan_rect)
#
#
#
#
#
# particle2 = ParticlePrinciple()
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         if event.type == PARTICLE_EVENT:
#             particle2.add_particles(-30, pygame.Color('Red'))
#             particle2.add_particles(-12, pygame.Color('Orange'))
#             particle2.add_particles(-6, pygame.Color('Yellow'))
#             particle2.add_particles(6, pygame.Color('Green'))
#             particle2.add_particles(10, pygame.Color('Blue'))
#             particle2.add_particles(30, pygame.Color('Purple'))
#
#
#
#
#
#     screen.fill((30, 30, 30))
#     particle2.emit()
#     pygame.display.update()
#     clock.tick(120)

# 20 июля
# def flatten(lst, depth=None):
#
#     def flatten_once(l):
#         result = []
#         for item in l:
#             if isinstance(item, list):
#                 result.extend(item)
#             else:
#                 result.append(item)
#         return result
#
#     if depth is None:
#
#         while any(isinstance(item, list) for item in lst):
#             lst = flatten_once(lst)
#         return lst
#     else:
#
#         for _ in range(depth):
#             if not any(isinstance(item, list) for item in lst):
#                 break
#             lst = flatten_once(lst)
#         return lst
#
#
# nested_list = [1, [2, [3, [4, 5], 6], 7], 8]
# print(flatten(nested_list))
# print(flatten(nested_list, 1))
# print(flatten(nested_list, 2))
# print(flatten(nested_list, 3))
# 25 июня скрин
# 27 июня
# from time import time, sleep
#
# def measure_time(func):
#
#
#     def decorator(*args, **kwargs):
#         t1 = time()
#         func(*args, **kwargs)
#         t2 = time()
#         delta = t2 - t1
#         return delta # возвращаем время работы функции
#
#     return decorator
#
# # Определение функций, время работы которых мы хотим измерить
# def f1():
#     """ Функция 1 """
#     sleep(0.5)
#     return 'f1 result'
#
# def f2():
#
#     sleep(0.5)
#     return 'f2 result'
#
# def f3():
#
#     sleep(1)
#     return 'f3 result'
#
#
# f1_decorated = measure_time(f1)
# f2_decorated = measure_time(f2)
# f3_decorated = measure_time(f3)
#
#
# time_of_f1 = f1_decorated()
# time_of_f2 = f2_decorated()
# time_of_f3 = f3_decorated()
#
# # Вывод времени работы функций
# print('Время работы f1:', round(time_of_f1, 2))
# print('Время работы f2:', round(time_of_f2, 2))
# print('Время работы f3:', round(time_of_f3, 2))

# 7 августа
# class Singleton:
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#         return cls._instance
#
#     def __init__(self, value=None):
#         if not hasattr(self, 'initialized'):
#             self.value = value
#             self.initialized = True
#
#
# singleton1 = Singleton("First Instance")
# print(singleton1.value)
#
# singleton2 = Singleton("Second Instance")
# print(singleton2.value)
#
#
# print(singleton1 is singleton2)
#
#
# print(id(singleton1))
# print(id(singleton2))


# from abc import ABC, abstractmethod
#
# # Абстрактный продукт A (например, Button)
# class Button(ABC):
#     @abstractmethod
#     def click(self):
#         pass
#
# # Абстрактный продукт B (например, Checkbox)
# class Checkbox(ABC):
#     @abstractmethod
#     def check(self):
#         pass
#
# # Конкретный продукт A1 (WindowsButton)
# class WindowsButton(Button):
#     def click(self):
#         return "Windows Button Clicked"
#
# # Конкретный продукт A2 (MacButton)
# class MacButton(Button):
#     def click(self):
#         return "Mac Button Clicked"
#
# # Конкретный продукт B1 (WindowsCheckbox)
# class WindowsCheckbox(Checkbox):
#     def check(self):
#         return "Windows Checkbox Checked"
#
# # Конкретный продукт B2 (MacCheckbox)
# class MacCheckbox(Checkbox):
#     def check(self):
#         return "Mac Checkbox Checked"
# class GUIFactory(ABC):
#     @abstractmethod
#     def create_button(self) -> Button:
#         pass
#
#     @abstractmethod
#     def create_checkbox(self) -> Checkbox:
#         pass
# class WindowsFactory(GUIFactory):
#     def create_button(self) -> Button:
#         return WindowsButton()
#
#     def create_checkbox(self) -> Checkbox:
#         return WindowsCheckbox()
#
# # Конкретная фабрика для macOS
# class MacFactory(GUIFactory):
#     def create_button(self) -> Button:
#         return MacButton()
#
#     def create_checkbox(self) -> Checkbox:
#         return MacCheckbox()
#
# def client_code(factory: GUIFactory):
#     button = factory.create_button()
#     checkbox = factory.create_checkbox()
#
#     print(button.click())
#     print(checkbox.check())
#
# if __name__ == "__main__":
#     print("Testing client code with WindowsFactory:")
#     client_code(WindowsFactory())
#
#     print("\nTesting client code with MacFactory:")
#     client_code(MacFactory())

# 31 июля
# 1
# user_role = 'manager'  # Можно менять на 'admin' или другие роли для тестирования
#
# def role_required(role: str):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             if user_role == role:
#                 return func(*args, **kwargs)
#             else:
#                 return 'Permission denied'
#         return wrapper
#     return decorator
#
# @role_required('admin')
# def secret_resource() -> str:
#     return 'Permission accepted'
#
# # Примеры использования
# print(secret_resource())  # Выведет 'Permission denied', так как роль 'manager'
# user_role = 'admin'
# print(secret_resource())
# 2
# RU_TO_EN = {
#     'привет': 'hello',
#     'мир': 'world',
#     'еда': 'food',
# }
#
# RU_TO_LT = {
#     'привет': 'sveiki',
#     'мир': 'pasaulis',
#     'еда': 'maistas',
# }
#
# def translate_to(lang: str):
#     def decorator(func):
#         def wrapper(word: str) -> str:
#             translation = word
#             if lang == 'EN':
#                 translation = RU_TO_EN.get(word, word)
#             elif lang == 'LT':
#                 translation = RU_TO_LT.get(word, word)
#             return translation
#         return wrapper
#     return decorator
#
# @translate_to('EN')
# def say(word: str) -> str:
#     return word
#
# # Примеры использования
# print(say('привет'))  #
# print(say('мир'))
#
#
# @translate_to('LT')
# def say_lithuanian(word: str) -> str:
#     return word
#
# print(say_lithuanian('привет'))
# print(say_lithuanian('мир'))
# 10 августа
#строчка import mvc_exceptions as mvc_exc не работает


#15 августа
#Задание 1 реализуйте класс который будет гарантировать, что только один его экземпляр может быть создан. Этот класс должен предоставлять метод для получения этого единственного экземпляра.
# class Singleton:
#     _instance = None  # Здесь будет храниться единственный экземпляр
#
#     @staticmethod
#     def get_instance():
#         if Singleton._instance is None:
#             Singleton._instance = Singleton()
#         return Singleton._instance
#
#     def __init__(self):
#         if Singleton._instance is not None:
#             raise Exception("Этот класс является синглтоном! Используйте метод get_instance() для получения экземпляра.")
#         else:
#             Singleton._instance = self
#
# # Примеры использования:
# singleton1 = Singleton.get_instance()
# singleton2 = Singleton.get_instance()
#
# print(singleton1 == singleton2)  # Выведет True, так как это один и тот же экземпляр

#2
# class Animal:
#     def speak(self):
#         pass
#
# class Dog(Animal):
#     def speak(self):
#         return "Woof!"
#
# class Cat(Animal):
#     def speak(self):
#         return "Meow!"
#
# class AnimalFactory:
#     @staticmethod
#     def create_animal(animal_type: str) -> Animal:
#         if animal_type == "dog":
#             return Dog()
#         elif animal_type == "cat":
#             return Cat()
#         else:
#             raise ValueError(f"Неизвестный тип животного: {animal_type}")
#
#
# factory = AnimalFactory()
#
# dog = factory.create_animal("dog")
# cat = factory.create_animal("cat")
#
# print(dog.speak())
# print(cat.speak())
#3
# class Observer:
#     def update(self, message: str):
#         pass
#
# class Subject:
#     def __init__(self):
#         self._observers = []
#
#     def attach(self, observer: Observer):
#         self._observers.append(observer)
#
#     def detach(self, observer: Observer):
#         self._observers.remove(observer)
#
#     def notify(self, message: str):
#         for observer in self._observers:
#             observer.update(message)
#
# # Пример конкретного наблюдателя:
# class ConcreteObserver(Observer):
#     def update(self, message: str):
#         print(f"Observer получил сообщение: {message}")
#
# # Примеры использования:
# subject = Subject()
#
# observer1 = ConcreteObserver()
# observer2 = ConcreteObserver()
#
# subject.attach(observer1)
# subject.attach(observer2)
#
# subject.notify("Изменение состояния")  # Оба наблюдателя получат сообщение
#
# subject.detach(observer1)
# subject.notify("Новое изменение состояния")  # Только observer2 получит сообщение








