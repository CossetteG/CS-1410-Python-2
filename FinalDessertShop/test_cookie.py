import unittest
from desserts import Cookie
from combine import Combinable

class DessertItemTest(unittest.TestCase):
  def setup(self):
    self.my_cookie = Cookie("cookie", 2, 3.00)
    self.my_cookie2 = Cookie("", 2, 2.30)   #not combinable 2
    self.my_cookie3 = Cookie("cookie", 0, 0.00)
    self.my_cookie4 = Cookie("", 0, 0.00)

    self.my_cookie6 = Cookie("cookie", 3, 3.00)#combinable
    self.my_cookie7 = Cookie("cookie", 2, 0.01)#not combinable

  def cookieinit(self, obj1, obj2, obj3, obj4):
    self.assertEqual(obj1.name, "cookie")
    self.assertEqual(obj2.name, "")
    self.assertEqual(obj3.name, "cookie") 
    self.assertEqual(type(obj3.name), str)
    self.assertEqual(obj4.name, "")

    self.assertEqual(obj1.cookie_quantity, 2) 
    self.assertEqual(obj2.cookie_quantity, 2 )
    self.assertEqual(type(obj2.cookie_quantity), int)
    self.assertEqual(obj3.cookie_quantity, 0)
    self.assertEqual(obj4.cookie_quantity, 0 )
    self.assertEqual(type(obj4.cookie_quantity), int)

    self.assertEqual(obj1.price_per_dozen, 3.00 )
    self.assertEqual(obj2.price_per_dozen, 2.30 )
    self.assertEqual(type(obj2.price_per_dozen), float)
    self.assertEqual(obj3.price_per_dozen, 0)
    self.assertEqual(obj4.price_per_dozen, 0 )
    self.assertEqual(type(obj4.price_per_dozen), float)

  def cookiemethods(self, obj1, obj2, obj3):
    self.assertEqual(obj1.calculate_cost(), 0.50)
    self.assertEqual(obj2.calculate_cost(), 0.38)
    self.assertEqual(obj3.calculate_cost(), 0.00)

  def test_combinable(self, obj1: "Combinable", obj2: "Combinable", obj3: "Combinable", obj4: "Combinable"):
    assert((isinstance(obj1, Cookie)) == True)
    assert((isinstance(obj2, Cookie)) == True)
    assert((isinstance(obj3, Cookie)) == True)
    assert((isinstance(obj4, Cookie)) == True)

    assert((obj1.can_combine(obj2))  == True)
    assert((obj1.can_combine(obj3)) == False)
    assert((obj1.can_combine(obj4)) == False)

    # print(obj1.combine(obj2))
    # cookie (Box), 5 cookies, $3.0/dozen, $1.25, $0.09

if __name__ == "__main__":
  mytest = DessertItemTest()
  mytest.setup()
  mytest.cookieinit(mytest.my_cookie, mytest.my_cookie2, mytest.my_cookie3, mytest.my_cookie4)
  mytest.cookiemethods(mytest.my_cookie, mytest.my_cookie2, mytest.my_cookie3)
  mytest.test_combinable(mytest.my_cookie, mytest.my_cookie6, mytest.my_cookie7, mytest.my_cookie2)
  print("done")