#desserts.py
#module
from abc import ABC, abstractmethod

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
    return [self.name, self.calculate_cost(), self.calculate_tax()]

class Candy(DessertItem):
  def __init__(self, name:str, candy_weight: float, price_per_pound: float):
    super().__init__(name)
    self.candy_weight = candy_weight
    self.price_per_pound = price_per_pound

  def calculate_cost(self):
    return round(self.price_per_pound * self.candy_weight, 2)


class Cookie(DessertItem):
  def __init__(self, name:str, cookie_quantity:int, price_per_dozen:float):
    super().__init__(name)
    self.cookie_quantity = cookie_quantity
    self.price_per_dozen = price_per_dozen

  def calculate_cost(self):
    return round((self.price_per_dozen/12 * self.cookie_quantity), 2)

class IceCream(DessertItem):
  def __init__(self, name:str, scoop_count:int, price_per_scoop:float):
    super().__init__(name)
    self.scoop_count = scoop_count
    self.price_per_scoop = price_per_scoop

  def calculate_cost(self):
    return round(self.price_per_scoop * self.scoop_count, 2)


class Sundae(IceCream):
  def __init__(self, name:str, scoop_count:int, price_per_scoop:float, topping_name:str, topping_price:float):
    super().__init__(name, scoop_count, price_per_scoop)
    self.topping_name = topping_name
    self.topping_price = topping_price 

  def calculate_cost(self):
    return round(self.price_per_scoop * self.scoop_count, 2) + self.topping_price


class Order:
   def __init__(self):
      self.order = []

   def add(self, dessert: DessertItem):
      self.order.append(dessert)

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
      data.append(item.receipt_input())
    data.append([self.order_cost(), self.order_tax(), self.order_cost() + self.order_tax()])
    return data 

#dessertshop.py
from desserts import Cookie, Candy, IceCream, Sundae, Order

def main():
   dessert_order = Order()
   dessert_order.add(Candy("Candy Corn", 1.5, .25))
   dessert_order.add(Candy("Gummy Bears", .25, .35))
   dessert_order.add(Cookie("Chocolate Chip", 6, 3.99))
   dessert_order.add(IceCream("Pistachio", 2, .79))
   dessert_order.add(Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29))
   dessert_order.add(Cookie("Oatmeal Raisin", 2, 3.45))
   print(dessert_order)
   return dessert_order

# main()

#receipt.py
# imports module
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from desserts import Order, Cookie, Candy, IceCream, Sundae
from dessertshop import main as _main
#there's a rounding difference but idgaf

def make_receipt(data:list[list[str,int,float]], out_file_name:str):
	"""makes a pdf receipt of our order"""
	

	# creating a Base Document Template of page size A4
	pdf = SimpleDocTemplate( out_file_name , pagesize = A4 )

	# standard stylesheet defined within reportlab itself
	styles = getSampleStyleSheet()

	# fetching the style of Top level heading (Heading1)
	title_style = styles[ "Heading1" ]

	# 0: left, 1: center, 2: right
	title_style.alignment = 1

	# creating the paragraph with
	# the heading text and passing the styles of it
	title = Paragraph( "Dessert Receipt" , title_style )

	# creates a Table Style object and in it,
	# defines the styles row wise
	# the tuples which look like coordinates
	# are nothing but rows and columns
	style = TableStyle(
		[
			( "BOX" , ( 0, 0 ), ( -1, -1 ), 1 , colors.black ),
			( "GRID" , ( 0, 0 ), ( 4 , 12 ), 1 , colors.black ),
			( "BACKGROUND" , ( 0, 0 ), ( 3, 0 ), colors.gray ),
			( "TEXTCOLOR" , ( 0, 0 ), ( -1, 0 ), colors.whitesmoke ),
			( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ),
			( "BACKGROUND" , ( 0 , 1 ) , ( -1 , -1 ), colors.beige ),
		]
	)

	# creates a table object and passes the style to it
	table = Table(data , style = style )

	# final step which builds the
	# actual pdf putting together all the elements
	pdf.build([ title , table ])

def main():
	dessert_order = _main()

	data = dessert_order.receipt_input()
	order_length = str(len(dessert_order))
	
	totals = data.pop()
	#conv_data = [[str(name), "$"+str(cost), "$"+str(tax)],  for [name, cost, tax] in data]
	conv_data = []
	for name, cost, tax in data:
		print_name = str(name)
		print_cost = "$"+str(cost)
		print_tax = "$"+str(tax)
		conv_data.append([print_name, "", print_cost, print_tax])
	conv_totals = [ "$"+str(price) for price in totals]

	# data which we are going to display as tables
	DATA = [
		[ "Name", "", "Item Cost", "Tax" ],] + conv_data + [
			"-"*56, "", ""] +[
		[ "Order Subtotals", "", conv_totals[0], conv_totals[1]],
		[ "Total", "", "", conv_totals[2]],
		[ "Total items in the order", "", "", order_length]
	]

	make_receipt(DATA, "receipt.pdf")
	print("done")

if __name__ == "__main__":
	main()
   
#test_candy.py
import unittest
from desserts import Candy

class DessertItemTest(unittest.TestCase):
  def setup(self):
    self.my_candy = Candy("candy", 3.00, 3.00)
    self.my_candy2 = Candy("", 0.00, 0.00)
    self.my_candy3 = Candy("candy", 1.5, 1.25)
    self.my_candy4 = Candy("", 1.5, 1.25)

  def candyinit(self, obj1, obj2, obj3, obj4):
    assert obj1.name == "candy"
    assert obj2.name == ""
    assert obj3.name == "candy" and type(obj3.name) == str
    assert obj4.name == ""

    assert obj1.candy_weight == 3.00
    assert obj2.candy_weight == 0.00 and type(obj1.candy_weight) == float
    assert obj3.candy_weight == 1.5
    assert obj4.candy_weight == 1.5 and type(obj3.candy_weight) == float

    assert obj1.price_per_pound == 3.00
    assert obj2.price_per_pound == 0.00 and type(obj1.price_per_pound) == float
    assert obj3.price_per_pound == 1.25
    assert obj4.price_per_pound == 1.25 and type(obj3.price_per_pound) == float

  def candymethods(self, obj1, obj2, obj3):
    assert obj1.calculate_cost() == 9.00
    assert obj2.calculate_cost() == 0.00
    assert obj3.calculate_cost() == 1.88


if __name__ == "__main__":
  mytest = DessertItemTest()
  mytest.setup()
  mytest.candyinit(mytest.my_candy, mytest.my_candy2, mytest.my_candy3, mytest.my_candy4)
  mytest.candymethods(mytest.my_candy, mytest.my_candy2, mytest.my_candy3)
  print("done")

#test_cookie.py
import unittest
from desserts import Cookie

class DessertItemTest(unittest.TestCase):
  def setup(self):
    self.my_cookie = Cookie("cookie", 2, 3.00)
    self.my_cookie2 = Cookie("", 2, 1.25)
    self.my_cookie3 = Cookie("cookie", 0, 0.00)
    self.my_cookie4 = Cookie("", 0, 0.00)

  def cookieinit(self, obj1, obj2, obj3, obj4):
    assert obj1.name == "cookie"
    assert obj2.name == ""
    assert obj3.name == "cookie" and type(obj3.name) == str
    assert obj4.name == ""

    assert obj1.cookie_quantity == 2 
    assert obj2.cookie_quantity == 2 and type(obj2.cookie_quantity) == int
    assert obj3.cookie_quantity == 0
    assert obj4.cookie_quantity == 0 and type(obj4.cookie_quantity) == int

    assert obj1.price_per_dozen == 3.00 
    assert obj2.price_per_dozen == 1.25 and type(obj2.price_per_dozen) == float
    assert obj3.price_per_dozen == 0
    assert obj4.price_per_dozen == 0 and type(obj4.price_per_dozen) == float

  def cookiemethods(self, obj1, obj2, obj3):
    assert obj1.calculate_cost() == 0.50
    assert obj2.calculate_cost() == 0.21
    assert obj3.calculate_cost() == 0.00

if __name__ == "__main__":
  mytest = DessertItemTest()
  mytest.setup()
  mytest.cookieinit(mytest.my_cookie, mytest.my_cookie2, mytest.my_cookie3, mytest.my_cookie4)
  mytest.cookiemethods(mytest.my_cookie, mytest.my_cookie2, mytest.my_cookie3)
  print("done")

#test_dessert.py
#testing
import unittest
from desserts import DessertItem, Candy, Cookie, Sundae, IceCream, Order

class DessertItemTest(unittest.TestCase):
  def setup(self):
    self.my_candy = Candy("dessert", 3.00, 3.00)
    self.my_candy2 = Candy("candy", 1.5, 1.25)
    self.my_cookie2 = Cookie("cookie", 2, 1.25)

    self.my_order = Order()
    self.my_order.add(self.my_candy)
    self.my_order.add(self.my_candy2)
    self.my_order.add(self.my_cookie2)

  def verify_lineage(self, des_obj, coo_obj, can_obj, ice_obj, sun_obj):
    assert issubclass(coo_obj, des_obj)
    assert issubclass(can_obj, des_obj)
    assert issubclass(ice_obj, des_obj)
    assert issubclass(sun_obj, ice_obj)


  def dessertinit(self, obj1, obj2):
    assert obj1.name == "dessert" and type(obj1.name) == str
    assert obj2.name == "candy"
    assert obj1.tax_percent == 7.25

  def dessertmethods(self, obj1, obj2, obj3):
    assert obj1.calculate_tax() == .65
    assert obj2.calculate_tax() == .14

    assert obj1.receipt_input() == ["dessert", 9.00, .65]
    assert obj2.receipt_input() == ["candy", 1.88, .14]
    assert obj3.receipt_input() == ["cookie", 0.21, .02]

  def ordermethods(self, obj):
    assert type(obj.order) == list
#     assert str(obj) == """dessert
# candy
# cookie
# Total number of items in order: 3

# """
    assert obj.order_cost() == 11.09
    assert obj.order_tax() == 0.81
    assert obj.receipt_input() == [['dessert', 9.00, 0.65], ['candy', 1.88, 0.14], ['cookie', 0.21, .02], [11.09, 0.81, 11.90]]

if __name__ == "__main__":
  mytest = DessertItemTest()
  mytest.setup()
  mytest.verify_lineage(DessertItem, Cookie, Candy, IceCream, Sundae)
  mytest.dessertinit(mytest.my_candy, mytest.my_candy2)
  mytest.dessertmethods(mytest.my_candy, mytest.my_candy2, mytest.my_cookie2)
  mytest.ordermethods(mytest.my_order)
  print("done")

#test_icecream.py
import unittest
from desserts import IceCream

class DessertItemTest(unittest.TestCase):
  def setup(self):
    self.my_icecream = IceCream("icecream", 2, 3.00)
    self.my_icecream2 = IceCream("", 2, 1.25)
    self.my_icecream3 = IceCream("icecream", 0, 0.00)
    self.my_icecream4 = IceCream("", 0, 0.00)

  def icecreaminit(self, obj1, obj2, obj3, obj4):
    assert obj1.name == "icecream"
    assert obj2.name == ""
    assert obj3.name == "icecream" and type(obj3.name) == str
    assert obj4.name == ""

    assert obj1.scoop_count == 2 
    assert obj2.scoop_count == 2 and type(obj2.scoop_count) == int
    assert obj3.scoop_count == 0
    assert obj4.scoop_count == 0 and type(obj4.scoop_count) == int

    assert obj1.price_per_scoop == 3.00 
    assert obj2.price_per_scoop == 1.25 and type(obj2.price_per_scoop) == float
    assert obj3.price_per_scoop == 0
    assert obj4.price_per_scoop == 0 and type(obj4.price_per_scoop) == float

  def icecreammethods(self, obj1, obj2, obj3):
    assert obj1.calculate_cost() == 6.00
    assert obj2.calculate_cost() == 2.50
    assert obj3.calculate_cost() == 0.00

if __name__ == "__main__":
  mytest = DessertItemTest()
  mytest.setup()
  mytest.icecreaminit(mytest.my_icecream, mytest.my_icecream2, mytest.my_icecream3, mytest.my_icecream4)
  mytest.icecreammethods(mytest.my_icecream, mytest.my_icecream2, mytest.my_icecream3)
  print("done")

#test_sundae.py
import unittest
from desserts import Sundae

class DessertItemTest(unittest.TestCase):
  def setup(self):
    self.my_sundae = Sundae("sundae", 2, 3.00, "topping", 3.00)
    self.my_sundae2 = Sundae("", 2, 1.25, "", 1.15)
    self.my_sundae3 = Sundae("sundae", 0, 0.00, "topping", 0.00)
    self.my_sundae4 = Sundae("", 0, 0.00, "", 0.00)

  def sundaeinit(self, obj1, obj2, obj3, obj4):
    assert obj1.name == "sundae"
    assert obj2.name == ""
    assert obj3.name == "sundae" and type(obj3.name) == str
    assert obj4.name == ""

    assert obj1.scoop_count == 2 
    assert obj2.scoop_count == 2 and type(obj2.scoop_count) == int
    assert obj3.scoop_count == 0
    assert obj4.scoop_count == 0 and type(obj4.scoop_count) == int

    assert obj1.price_per_scoop == 3.00 
    assert obj2.price_per_scoop == 1.25 and type(obj2.price_per_scoop) == float
    assert obj3.price_per_scoop == 0
    assert obj4.price_per_scoop == 0  and type(obj4.price_per_scoop) == float

    assert obj1.topping_name == "topping"
    assert obj2.topping_name == ""
    assert obj3.topping_name == "topping" and type(obj3.topping_name) == str
    assert obj4.topping_name == ""

    assert obj1.topping_price == 3.00 
    assert obj2.topping_price == 1.15 and type(obj2.topping_price) == float
    assert obj3.topping_price == 0
    assert obj4.topping_price == 0  and type(obj4.topping_price) == float

  def sundaemethods(self, obj1, obj2, obj3):
    assert obj1.calculate_cost() == 9.00
    assert obj2.calculate_cost() == 3.65
    assert obj3.calculate_cost() == 0.00

if __name__ == "__main__":
  mytest = DessertItemTest()
  mytest.setup()
  mytest.sundaeinit(mytest.my_sundae, mytest.my_sundae2, mytest.my_sundae3, mytest.my_sundae4)
  mytest.sundaemethods(mytest.my_sundae, mytest.my_sundae2, mytest.my_sundae3)
  print("done")  