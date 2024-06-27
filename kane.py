class Car:
    def __init__(self):
        self.model = ""
        self.year = 0
        self.manufacturer = ""
        self.engine_capacity = 0.0
        self.color = ""
        self.price = 0.0

    def input_data(self):
        self.model = input("Enter car model: ")
        self.year = input("Enter year of manufacture: ")
        self.manufacturer = input("Enter manufacturer: ")
        self.engine_capacity = float(input("Enter engine capacity: "))
        self.color = input("Enter car color: ")
        self.price = float(input("Enter car price: "))

    def output_data(self):
        print("Car Model:", self.model)
        print("Year of Manufacture:", self.year)
        print("Manufacturer:", self.manufacturer)
        print("Engine Capacity:", self.engine_capacity)
        print("Color:", self.color)
        print("Price:", self.price)

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_manufacturer(self):
        return self.manufacturer

    def get_engine_capacity(self):
        return self.engine_capacity

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price


class Book:
    def __init__(self):
        self.title = ""
        self.year = 0
        self.publisher = ""
        self.genre = ""
        self.author = ""
        self.price = 0.0

    def input_data(self):
        self.title = input("Enter book title: ")
        self.year = input("Enter year of publication: ")
        self.publisher = input("Enter publisher: ")
        self.genre = input("Enter genre: ")
        self.author = input("Enter author: ")
        self.price = float(input("Enter book price: "))

    def output_data(self):
        print("Book Title:", self.title)
        print("Year of Publication:", self.year)
        print("Publisher:", self.publisher)
        print("Genre:", self.genre)
        print("Author:", self.author)
        print("Price:", self.price)

    def get_title(self):
        return self.title

    def get_year(self):
        return self.year

    def get_publisher(self):
        return self.publisher

    def get_genre(self):
        return self.genre

    def get_author(self):
        return self.author

    def get_price(self):
        return self.price


class Stadium:
    def __init__(self):
        self.name = ""
        self.opening_date = ""
        self.country = ""
        self.city = ""
        self.capacity = 0

    def input_data(self):
        self.name = input("Enter stadium name: ")
        self.opening_date = input("Enter opening date: ")
        self.country = input("Enter country: ")
        self.city = input("Enter city: ")
        self.capacity = int(input("Enter stadium capacity: "))

    def output_data(self):
        print("Stadium Name:", self.name)
        print("Opening Date:", self.opening_date)
        print("Country:", self.country)
        print("City:", self.city)
        print("Capacity:", self.capacity)

    def get_name(self):
        return self.name

    def get_opening_date(self):
        return self.opening_date

    def get_country(self):
        return self.country

    def get_city(self):
        return self.city

    def get_capacity(self):
        return self.capacity
car = Car()
car.input_data()
car.output_data()


book = Book()
book.input_data()
book.output_data()


stadium = Stadium()
stadium.input_data()
stadium.output_data()