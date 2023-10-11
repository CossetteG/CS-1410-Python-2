"""
Dessert Shop!!
:( you never let me have any fun
"""
#module
class DessertItem:
  def __init__(self, name: str):
    self.name = name

class Candy(DessertItem):
  def __init__(self, name:str, weight: float, price_per_pound: float):
    super().__init__(name)
    self.weight = weight
    self.price_per_pound = price_per_pound

class Cookie(DessertItem):
  def __init__(self, name:str, quantity:int, price_per_dozen:float):
    super().__init__(name)
    self.quantity = quantity
    self.price_per_pound = price_per_dozen

class IceCream(DessertItem):
  def __init__(self, name:str, scoop_count:int, price_per_scoop:float):
    super().__init__(name)
    self.scoop_count = scoop_count
    self.price_per_scoop = price_per_scoop

class Sundae(IceCream):
  def __init__(self, name:str, scoop_count:int, price_per_scoop:float, topping_name:str, topping_price:float):
    super().__init__(name, scoop_count, price_per_scoop)
    self.topping_name = topping_name
    self.topping_price = topping_price 

my_des = Sundae("bleh", 5, 5, 5, 5)

#testing
import unittest
#from dessert import DessertItem, Cookie, Candy, IceCream, Sundae

class DessertItemTest(unittest.TestCase):
  def setup(self):
    self.my_dessert = DessertItem("dessert")
    self.my_dessert2 = DessertItem("")

    self.my_cookie = Cookie("cookie", 2, 3.00)
    self.my_cookie2 = Cookie("", 2, 3.00)
    self.my_cookie3 = Cookie("cookie", 0, 0.00)
    self.my_cookie4 = Cookie("", 0, 0.00)

    self.my_candy = Candy("candy", 3.00, 3.00)
    self.my_candy2 = Candy("", 3.00, 3.00)
    self.my_candy3 = Candy("candy", 0.00, 0.00)
    self.my_candy4 = Candy("", 0.00, 0.00)

    self.my_icecream = IceCream("icecream", 2, 3.00)
    self.my_icecream2 = IceCream("", 2, 3.00)
    self.my_icecream3 = IceCream("icecream", 0, 0.00)
    self.my_icecream4 = IceCream("", 0, 0.00)

    self.my_sundae = Sundae("sundae", 2, 3.00, "topping", 3.00)
    self.my_sundae2 = Sundae("", 2, 3.00, "", 3.00)
    self.my_sundae3 = Sundae("sundae", 0, 0.00, "topping", 0.00)
    self.my_sundae4 = Sundae("", 0, 0.00, "", 0.00)


  def verify_lineage(self, des_obj, coo_obj, can_obj, ice_obj, sun_obj):
    assert issubclass(coo_obj, des_obj)
    assert issubclass(can_obj, des_obj)
    assert issubclass(ice_obj, des_obj)
    assert issubclass(sun_obj, ice_obj)

  def dessertinit(self, obj1, obj2):
    assert obj1.name == "dessert" and type(obj1.name) == str
    assert obj2.name == ""

  def cookieinit(self, obj1, obj2, obj3, obj4):
    assert obj1.name == "cookie"
    assert obj2.name == ""
    assert obj3.name == "cookie"
    assert obj4.name == ""

    assert obj1.quantity == 2 and type(obj1.quantity) == str
    assert obj2.quantity == 2
    assert obj3.quantity == 0
    assert obj4.quantity == 0 

    assert obj1.price_per_pound == 3.00 and type(obj1.quantity) == float
    assert obj2.quantity == 2
    assert obj3.quantity == 0
    assert obj4.quantity == 0 

  def candyinit(self, obj1, obj2, obj3, obj4):
    assert obj1.name == "cookie"
    assert obj2.name == ""
    assert obj3.name == "cookie"
    assert obj4.name == ""

    assert obj1.quantity == 2 and type(obj1.quantity) == str
    assert obj2.quantity == 2
    assert obj3.quantity == 0
    assert obj4.quantity == 0 

    assert obj1.price_per_pound == 3.00 and type(obj1.quantity) == float
    assert obj2.quantity == 2
    assert obj3.quantity == 0
    assert obj4.quantity == 0

  def icecreaminit(self, obj1, obj2, obj3, obj4):
    assert obj1.name == "cookie"
    assert obj2.name == ""
    assert obj3.name == "cookie"
    assert obj4.name == ""

    assert obj1.quantity == 2 and type(obj1.quantity) == str
    assert obj2.quantity == 2
    assert obj3.quantity == 0
    assert obj4.quantity == 0 

    assert obj1.price_per_pound == 3.00 and type(obj1.quantity) == float
    assert obj2.quantity == 2
    assert obj3.quantity == 0
    assert obj4.quantity == 0 

  def sundaeinit(self, obj1, obj2, obj3, obj4):
    assert obj1.name == "cookie"
    assert obj2.name == ""
    assert obj3.name == "cookie"
    assert obj4.name == ""

    assert obj1.quantity == 2 and type(obj1.quantity) == str
    assert obj2.quantity == 2
    assert obj3.quantity == 0
    assert obj4.quantity == 0 

    assert obj1.price_per_pound == 3.00 and type(obj1.quantity) == float
    assert obj2.quantity == 2
    assert obj3.quantity == 0
    assert obj4.quantity == 0 
  
#gotta finish
if __name__ == "__main__":
  mytest = DessertItemTest()
  mytest.setup()
  mytest.verify_lineage(DessertItem, Cookie, Candy, IceCream, Sundae)
  
  print("yes")