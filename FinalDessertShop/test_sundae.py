import unittest
from desserts import Sundae

class DessertItemTest(unittest.TestCase):
  def setup(self):
    self.my_sundae = Sundae("sundae", 2, 3.00, "topping", 3.00)
    self.my_sundae2 = Sundae("", 2, 2.30, "", 1.15)
    self.my_sundae3 = Sundae("sundae", 0, 0.00, "topping", 0.00)
    self.my_sundae4 = Sundae("", 0, 0.00, "", 0.00)

  def sundaeinit(self, obj1, obj2, obj3, obj4):
    self.assertEqual(obj1.name, "sundae")
    self.assertEqual(obj2.name, "")
    self.assertEqual(obj3.name, "sundae")
    self.assertEqual(type(obj3.name), str)
    self.assertEqual(obj4.name, "")

    self.assertEqual(obj1.scoop_count, 2 )
    self.assertEqual(obj2.scoop_count, 2)
    self.assertEqual(type(obj2.scoop_count), int)
    self.assertEqual(obj3.scoop_count, 0)
    self.assertEqual(obj4.scoop_count, 0)
    self.assertEqual(type(obj4.scoop_count), int)

    self.assertEqual(obj1.price_per_scoop, 3.00)
    self.assertEqual(obj2.price_per_scoop, 2.30) 
    self.assertEqual(type(obj2.price_per_scoop), float)
    self.assertEqual(obj3.price_per_scoop, 0)
    self.assertEqual(obj4.price_per_scoop, 0)
    self.assertEqual(type(obj4.price_per_scoop), float)

    self.assertEqual(obj1.topping_name, "topping")
    self.assertEqual(obj2.topping_name, "")
    self.assertEqual(obj3.topping_name, "topping")
    self.assertEqual(type(obj3.topping_name), str)
    self.assertEqual(obj4.topping_name, "")

    self.assertEqual(obj1.topping_price, 3.00)
    self.assertEqual(obj2.topping_price, 1.15)
    self.assertEqual(type(obj2.topping_price), float)
    self.assertEqual(obj3.topping_price, 0)
    self.assertEqual(obj4.topping_price, 0 )
    self.assertEqual(type(obj4.topping_price), float)

  def sundaemethods(self, obj1, obj2, obj3):
    self.assertEqual(obj1.calculate_cost(), 9.00)
    self.assertEqual(obj2.calculate_cost(), 5.75)
    self.assertEqual(obj3.calculate_cost(), 0.00)

if __name__ == "__main__":
  mytest = DessertItemTest()
  mytest.setup()
  mytest.sundaeinit(mytest.my_sundae, mytest.my_sundae2, mytest.my_sundae3, mytest.my_sundae4)
  mytest.sundaemethods(mytest.my_sundae, mytest.my_sundae2, mytest.my_sundae3)
  print("done")