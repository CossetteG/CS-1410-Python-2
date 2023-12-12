#module
from abc import ABC, abstractmethod
from packaging import Packaging
from combine import Combinable
# import sqlalchemy.types as types

class DessertItem(ABC):
  tax_percent:float = 7.25

  def __init__(self, name: str):
    self.name = name

  @abstractmethod
  def calculate_cost(price:float):
    """calculates price without tax, round everthing to 2 decimal"""
    pass 

  def calculate_tax(self):
    return round(self.calculate_cost() * self.tax_percent/100, 2)

  def receipt_input(self):
    input = [self.name, None, None, self.calculate_cost(), self.calculate_tax()]

  def __eq__(self, other):
    if self.calculate_cost() == other.calculate_cost():
      return True
    else:
      return False

  def __neq__(self, other):
    if self.calculate_cost() != other.calculate_cost():
      return True
    else:
      return False

  def __lt__(self, other):
    if self.calculate_cost() < other.calculate_cost():
      return True
    else:
      return False

  def __gt__(self, other):
    if self.calculate_cost() > other.calculate_cost():
      return True 
    else:
      return False

  def __le__(self, other):
    if self.calculate_cost() <= other.calculate_cost():
      return True
    else:
      return False

  def __ge__(self, other):
    if self.calculate_cost() >= other.calculate_cost():
      return True
    else:
      return False


    
class Candy(DessertItem):
  def __init__(self, name:str, candy_weight: float, price_per_pound: float, packaging:str="(Bag)"):
    super().__init__(name)
    self.candy_weight = candy_weight
    self.price_per_pound = price_per_pound
    self.packaging = packaging
  
  def calculate_cost(self):
    return round(self.price_per_pound * self.candy_weight, 2)
  
  def receipt_input(self):
    input = [self.name +" "+ self.packaging, str(self.candy_weight) + "lbs", "$" + str(self.price_per_pound) + "/lb", "$" + str(self.calculate_cost()), "$" + str(self.calculate_tax())]
    return input 

  def __str__(self):
    namepack = self.name+" "+ self.packaging
    return f"{namepack}, {self.candy_weight} lbs, $" + str(self.price_per_pound) + "/lbs, $" + str(self.calculate_cost()) + ", $" + str(self.calculate_tax())

  def can_combine(self, other: "Candy") -> True:
    if isinstance(other, Candy) and other.name == self.name and other.price_per_pound == self.price_per_pound:
      return True
    else:
      return False

  def combine(self, other: "Candy")-> "Candy":
    self.candy_weight += other.candy_weight 
    del(other)
    return self


class Cookie(DessertItem):
  def __init__(self, name:str, cookie_quantity:int, price_per_dozen:float, packaging:str="(Box)"):
    super().__init__(name)
    self.cookie_quantity = cookie_quantity
    self.price_per_dozen = price_per_dozen
    self.packaging = packaging

  def calculate_cost(self):
    return round((self.price_per_dozen/12 * self.cookie_quantity), 2)

  def receipt_input(self):
    input = [self.name+" "+ self.packaging, str(self.cookie_quantity) + " cookies", "$" + str(self.price_per_dozen) + "/dozen", "$" + str(self.calculate_cost()), "$" + str(self.calculate_tax())]
    return input 

  def __str__(self):
    namepack = self.name+" "+ self.packaging
    return f"{namepack}, {self.cookie_quantity} cookies, $" + str(self.price_per_dozen) + "/dozen, $" + str(self.calculate_cost()) + ", $" + str(self.calculate_tax())

  def can_combine(self, other:"Candy") ->True:
    if isinstance(other, Cookie) and self.name == other.name and self.price_per_dozen == other.price_per_dozen:
      return True 
    else:
      return False

  def combine(self, other: "Cookie") -> "Cookie":
    self.cookie_quantity += other.cookie_quantity
    del(other)
    return self

class IceCream(DessertItem):
  def __init__(self, name:str, scoop_count:int, price_per_scoop:float, packaging:str="(Bowl)"):
    super().__init__(name)
    self.scoop_count = scoop_count
    self.price_per_scoop = price_per_scoop
    self.packaging = packaging

  def calculate_cost(self):
    return round(self.price_per_scoop * self.scoop_count, 2)

  def receipt_input(self):
    input = [self.name+" "+ self.packaging, str(self.scoop_count) + " scoops", "$" + str(self.price_per_scoop) + "/scoop", "$" + str(self.calculate_cost()), "$" + str(self.calculate_tax())]
    return input 

  def __str__(self):
    return f"{self.name} Ice Cream {self.packaging}, {self.scoop_count} scoops, ${self.price_per_scoop}/scoop, ${self.calculate_cost()}, ${self.calculate_tax()}"


class Sundae(IceCream):
  def __init__(self, name:str, scoop_count:int, price_per_scoop:float, topping_name:str, topping_price:float, packaging:str="(Boat)"):
    super().__init__(name, scoop_count, price_per_scoop)
    self.topping_name = topping_name
    self.topping_price = topping_price 
    self.packaging = packaging

  def calculate_cost(self):
    return round(self.price_per_scoop * self.scoop_count + self.topping_price, 2)

  def receipt_input(self):
    input = [self.name+" "+ self.packaging, str(self.scoop_count) + " scoops", "$" + str(self.price_per_scoop) + "/scoop", "$" + str(self.calculate_cost()), "$" + str(self.calculate_tax()), "  " + self.topping_name, "$" + str(self.topping_price)]
    return input 

  def __str__(self):
    return f"{self.name} Ice Cream {self.packaging}, {self.scoop_count} scoops, ${self.price_per_scoop}/scoop, ${self.calculate_cost()}, ${self.calculate_tax()}, {self.topping_name}, ${self.topping_price}"


class Order:
   legal_values = {"CASH", "CARD", "PHONE"}
   def __init__(self, PayType="CASH"):
      self.order = []
      self.PayType = PayType

   def add(self, dessert: DessertItem):
      if isinstance(dessert, Candy) or isinstance(dessert, Cookie): 
        # print("check 1")
        cache = False
        for item in self.order[::-1]:
          # print("check 2")
          if dessert.can_combine(item):
            # print("check 3")
            cache = True
            item.combine(dessert)
        if cache == True:
          # print("check 6")
          pass
        else:
          self.order.append(dessert)
          # print("check 4")
      else:
        self.order.append(dessert)
        # print("check 5")

   def __len__(self):
      return len(self.order)

   def __str__(self):
      namelist = [item.name for item in self.order]
      namelist.append(f"Total number of items in order: {len(self)}")
      namestring = ''''''
      for itemm in namelist:
         namestring += itemm
         namestring += '''
'''   
      namestring += f", PayType: {self.PayType}"
      return namestring

   def order_cost(self):
      subtotal = 0.00
      for item in self.order:
        subtotal += item.calculate_cost()
      return round(subtotal, 2)
    
   def order_tax(self):
      tax_total = 0.00
      for item in self.order:
        tax_total += item.calculate_tax()
      return round(tax_total, 2)

   def receipt_input(self):
    data = []
    for item in self.order:
      input = item.receipt_input()
      if len(input) == 5:
        data.append(input) #list of 5 strings
      else:
        data.append(input[0:5]) #list of 5
        data.append(input[5:7]) #list of 2
    data.append([self.order_cost(), self.order_tax(), self.order_cost() + self.order_tax(), self.PayType])
    return data 

   def get_pay_type(self):
    return self.PayType 

   def set_pay_type(self, paytype):
    if paytype in self.legal_values:
      self.PayType = paytype
    else:
      raise ValueError("That PayType is not allowed")

   def __add__(self, other):
      self.order += other.order

