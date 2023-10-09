'''
there will be a final project idea and final project design due later this month
start thinking about what you want for your final project
we will be using a user interface with our projects
'''

#Importing Modules and Importing Functions - should be done
#Advanced- getting stuff from a different file and putting it into classes

import csv
from module import apps.csv as csv_file

class App:
    def __init__(self, name, description, category):
        self.name = name
        self.description = description
        self.category = category

    def display(self):
        return self.name
    
    def __repr__(self):
        return f"{self.name} is a {self.category} app."
    #overriding the dender method to represent oneself
    #this will now print this instead of the location when an instance is called
    
    def __str__(self):
        return f"{self.name} is used to {self.description}"
    #will only work for one object, doesn't work in a list
    #is always called over __repr__

apps = []

with open("apps.csv") as csv_file:
    csv_reader = csv.reader("apps.csv", delimiter=',')
    print(csv_reader)
    for name in csv_reader:
       print(name)
        # apps.append(App(name, description, category))


# print(apps) 
# my_obj = App("Pinterest", "scroll cute pics", "social media")
# print(repr(my_obj)) 
# print(str(my_obj))
# print(my_obj)

# Class composition 
class Car:
    def __init__(self, color, engine):
        self.color = color
        self.engine = engine

    def describe(self):
        print(f'{self.color} car')
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def revv(self):
        print("vroom vroom")

my_engine = Engine(450)
my_car = Car("black", my_engine)
my_car.describe()
my_car.engine.revv()


class Candy:
  def __init__(self, name, weight, price_per_pound):
    self.name = name
    self.weight = weight
    self.price_per_pound = price_per_pound

class Cookie:
  def __init__(self, name, quantity, price_per_pound):
    self.name = name
    self.quantity = quantity
    self.price_per_pound = price_per_pound

class IceCream:
  def __init__(self, name, scoop_count, price_per_scoop):
    self.name = name 
    self.scoop_count = scoop_count
    self.price_per_scoop = price_per_scoop

class Sundae(IceCream):
  def __init__(self, name, scoop_count, price_per_scoop, topping_name, topping_price):
    super().__init__(name, scoop_count, price_per_scoop)
    self.topping_name = topping_name
    self.topping_price = topping_price 

my_des = Sundae("bleh", 5, 5, 5, 5)
