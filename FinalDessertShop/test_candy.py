import unittest
from desserts import Candy

class DessertItemTest(unittest.TestCase):
  def setUp(self):
    self.my_candy = Candy("candy", 3.00, 3.00)
    self.my_candy2 = Candy("", 0.00, 0.00)
    self.my_candy3 = Candy("candy", 1.5, 2.30)
    self.my_candy4 = Candy("", 1.5, 2.30)

    self.my_candy6 = Candy("candy", 4.00, 3.00)
    self.my_candy7 = Candy("", 3.00, 3.00)

  def testcandyinit(self, obj1, obj2, obj3, obj4):
    self.assertEqual(obj1.name, "candy")
    self.assertEqual(obj2.name, "")
    self.assertEqual(obj3.name, "candy") 
    self.assertEqual(type(obj3.name), str)
    self.assertEqual(obj4.name, "")

    self.assertEqual(obj1.candy_weight, 3.00)
    self.assertEqual(obj2.candy_weight, 0.00 )
    self.assertEqual(type(obj1.candy_weight), float)
    self.assertEqual(obj3.candy_weight, 1.5)
    self.assertEqual(obj4.candy_weight, 1.5 )
    self.assertEqual(type(obj3.candy_weight), float)

    self.assertEqual(obj1.price_per_pound, 3.00)
    self.assertEqual(obj2.price_per_pound, 0.00 )
    self.assertEqual(type(obj1.price_per_pound), float)
    self.assertEqual(obj3.price_per_pound, 2.30)
    self.assertEqual(obj4.price_per_pound, 2.30 )
    self.assertEqual(type(obj3.price_per_pound), float)

  def testcandymethods(self, obj1, obj2, obj3):
    self.assertEqual(obj1.calculate_cost(), 9.00)
    self.assertEqual(obj2.calculate_cost(), 0.00)
    self.assertEqual(obj3.calculate_cost(), 3.45)

  def test_combinable(self, obj1: "Combinable", obj2: "Combinable", obj3: "Combinable", obj4: "Combinable"):
    assert((isinstance(obj1, Candy))== True)
    assert((isinstance(obj2, Candy))== True)
    assert((isinstance(obj3, Candy))== True)
    assert((isinstance(obj4, Candy))== True)

    assert((obj1.can_combine(obj2))== True)
    assert((obj1.can_combine(obj3))== False)
    assert((obj1.can_combine(obj4))== False)

    # print(obj1.combine(obj2)) 
    #candy (Bag), 7.0 lbs, $3.0/lbs, $21.0, $1.52


if __name__ == "__main__":
  # mytest = DessertItemTest()
  # mytest.setUp()
  # mytest.testcandyinit(mytest.my_candy, mytest.my_candy2, mytest.my_candy3, mytest.my_candy4)
  # mytest.testcandymethods(mytest.my_candy, mytest.my_candy2, mytest.my_candy3)
  # mytest.test_combinable(mytest.my_candy, mytest.my_candy6, mytest.my_candy7, mytest.my_candy2)
  unittest.main()
  print("done")