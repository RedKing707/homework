# Task 1
class Animal:
    def make_sound(self, sound):
        self.sound = sound
        return f"Voice of {self.__class__.__name__} == {self.sound}"


class Dog(Animal):
    pass


class Cow(Animal):
    pass


class Cat(Animal):
    pass


dog = Dog()
print(dog.make_sound(sound="Wof Wof Wof"))

cow = Cow()
print(cow.make_sound(sound="Moooooooooouuuuuuuwwwww"))

cat = Cat()
print(cat.make_sound(sound="Meow Meow Meow"))

# Task 2


class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        return (f"Brand of {self.__class__.__name__} == {self.brand}\n"
                f"Year of production == {self.year}")


vehicle = Vehicle(brand="Mercedes", year=2022)
print(vehicle.display_info())

print() # --> Этот print для отступа между выводами в терминале


class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self.doors = doors

    def display_info(self):
        return (f"Brand of {self.__class__.__name__} == {self.brand}\n"
                f"Year of production == {self.year}\n"
                f"Number of doors == {self.doors}")


car = Car(brand="BMW", year=2021, doors=4)
print(car.display_info())

print() # --> Этот print для отступа между выводами в терминале


class Motorcycle(Vehicle):
    def __init__(self, brand, year, wheels):
        super().__init__(brand, year)
        self.wheels = wheels

    def display_info(self):
        return (f"Brand of {self.__class__.__name__} == {self.brand}\n"
                f"Year of production == {self.year}\n"
                f"Number of wheels == {self.wheels}")


moto = Motorcycle(brand="Kawasaki", year=2020, wheels=2)
print(moto.display_info())





# Another Homewrok

# Task 1

class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def get_information(self):
        print(f"Имя: {self.name}\n"
              f"Возраст: {self.age}\n"
              f"Позиция: {self.position}\n"
              f"Зарплата: {self.salary}")

    def raise_position(self, new_position):
        self.position = new_position

    def raise_salary(self, amount):
        self.salary =+ amount


name = input("Добро пожаловать! Введите имя: ")
age = int(input("Введите возраст: "))
position = input("Введите позицию сотрудника: ")
salary = int(input("Зарплата: "))

employee = Employee(name=name, age=age, position=position, salary=salary)

while True:
    choise = int(input("Что хотите сделать: 1 - Информация, 2 - Повысить должность, 3 - Повысить зарплату, 4 - выход -  "))

    if choise == 1:
        print(employee.get_information())

    elif choise == 2:
        new_position = input("Введите новый должность: ")
        employee.raise_position(new_position)

    elif choise == 3:
        new_salary = int(input("Введите новую зарплату: "))
        employee.raise_salary(new_salary)
    else:
        break


# Task 2

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return (f"Привет я {self.name}\n"
                f"Мне {self.age}")


person1 = Person(name="Muhammad", age=18)
person2 = Person(name="Alex", age=20)

print(person1.get_info())
print(person2.get_info())