import unittest
from desserts import IceCream

class DessertItemTest(unittest.TestCase):
  def setup(self):
    self.my_icecream = IceCream("icecream", 2, 3.00)
    self.my_icecream2 = IceCream("", 2, 2.30)
    self.my_icecream3 = IceCream("icecream", 0, 0.00)
    self.my_icecream4 = IceCream("", 0, 0.00)

  def icecreaminit(self, obj1, obj2, obj3, obj4):
    self.assertEqual(obj1.name, "icecream")
    self.assertEqual(obj2.name, "")
    self.assertEqual(obj3.name, "icecream") 
    self.assertEqual(type(obj3.name), str)
    self.assertEqual(obj4.name, "")

    self.assertEqual(obj1.scoop_count, 2) 
    self.assertEqual(obj2.scoop_count, 2 )
    self.assertEqual(type(obj2.scoop_count), int)
    self.assertEqual(obj3.scoop_count, 0)
    self.assertEqual(obj4.scoop_count, 0 )
    self.assertEqual(type(obj4.scoop_count), int)

    self.assertEqual(obj1.price_per_scoop, 3.00 )
    self.assertEqual(obj2.price_per_scoop, 2.30 )
    self.assertEqual( type(obj2.price_per_scoop), float)
    self.assertEqual(obj3.price_per_scoop, 0)
    self.assertEqual(obj4.price_per_scoop, 0 )
    self.assertEqual( type(obj4.price_per_scoop), float)

  def icecreammethods(self, obj1, obj2, obj3):
    self.assertEqual(obj1.calculate_cost(), 6.00)
    self.assertEqual(obj2.calculate_cost(), 4.60)
    self.assertEqual(obj3.calculate_cost(), 0.00)

if __name__ == "__main__":
  mytest = DessertItemTest()
  mytest.setup()
  mytest.icecreaminit(mytest.my_icecream, mytest.my_icecream2, mytest.my_icecream3, mytest.my_icecream4)
  mytest.icecreammethods(mytest.my_icecream, mytest.my_icecream2, mytest.my_icecream3)
  print("done")