#testing
import unittest
from desserts import DessertItem, Candy, Cookie, Sundae, IceCream, Order
from packaging import Packaging
from payment import Payable 

class DessertItemTest(unittest.TestCase):
  def setup(self):
    self.my_candy = Candy("dessert", 3.00, 3.00)
    self.my_candy2 = Candy("candy", 1.5, 2.30)
    self.my_sundae = Sundae("cookiesncream", 2, 2.30, "fudge", .60)

    self.my_order = Order()
    self.my_order.add(self.my_candy)
    self.my_order.add(self.my_candy2)
    self.my_order.add(self.my_sundae)

  def verify_lineage(self, des_obj, coo_obj, can_obj, ice_obj, sun_obj):
    self.assertEqual(issubclass(coo_obj, des_obj), True)
    self.assertEqual(issubclass(can_obj, des_obj), True)
    self.assertEqual(issubclass(ice_obj, des_obj), True)
    self.assertEqual(issubclass(sun_obj, ice_obj), True)


  def dessertinit(self, obj1, obj2):
    self.assertEqual(obj1.name, "dessert" )
    self.assertEqual(type(obj1.name), str)
    self.assertEqual(obj2.name, "candy")
    self.assertEqual(obj1.tax_percent, 7.25)

  def dessertmethods(self, obj1, obj2, obj3):
    self.assertEqual(obj1.calculate_tax(), .65)
    self.assertEqual(obj2.calculate_tax(), .25)

    self.assertEqual(obj1.receipt_input(), ['dessert (Bag)', '3.0lbs', '$3.0/lb', '$9.0', '$0.65'])
    self.assertEqual(obj2.receipt_input(), ['candy (Bag)', '1.5lbs', '$2.3/lb', '$3.45', '$0.25'])
    # print(obj2.receipt_input())
    self.assertEqual(obj3.receipt_input(), ['cookiesncream (Boat)', '2 scoops', '$2.3/scoop', '$5.2', '$0.38', '  fudge', '$0.6'])
    # print(obj3.receipt_input())

  def ordermethods(self, obj):
    self.assertEqual(type(obj.order), list)

    self.assertEqual(obj.order_cost(), 17.65)
    self.assertEqual(obj.order_tax(), 1.28)
    self.assertEqual(obj.receipt_input(), [['dessert (Bag)', '3.0lbs', '$3.0/lb', '$9.0', '$0.65'], ['candy (Bag)', '1.5lbs', '$2.3/lb', '$3.45', '$0.25'], ['cookiesncream (Boat)', '2 scoops', '$2.3/scoop', '$5.2', '$0.38'], ['  fudge', '$0.6'], [17.65, 1.28, 18.93, "CASH"]])
    # print(obj.receipt_input())

  def test_str(self, obj, obj2, obj3):
    # print(obj)
    self.assertEqual(str(obj), "dessert (Bag), 3.0 lbs, $3.0/lbs, $9.0, $0.65")
    # print(obj2)
    self.assertEqual(str(obj2), "candy (Bag), 1.5 lbs, $2.3/lbs, $3.45, $0.25")
    # print(obj3)
    self.assertEqual(str(obj3), "cookiesncream Ice Cream (Boat), 2 scoops, $2.3/scoop, $5.2, $0.38, fudge, $0.6")

  def test_packaging(self, obj1, obj2, obj3, obj4):
    self.assertEqual((isinstance(obj1, Packaging)), True)
    self.assertEqual((isinstance(obj2, Packaging)), True)
    self.assertEqual((isinstance(obj3, Packaging)), True)
    self.assertEqual((isinstance(obj4, Packaging)), True)

  def test_paytype(self, obj1):
    self.assertEqual(isinstance(obj1, Payable), True)
    self.assertEqual((obj1.get_pay_type()), "CASH")
    obj1.set_pay_type("PHONE")
    self.assertEqual((obj1.get_pay_type()), "PHONE")
    self.assertRaises(ValueError, obj1.set_pay_type, "BLYAT")

  def test_sort(self, item1, item2, obj1):
    self.assertEqual(item1.calculate_cost(), 9.0)
    self.assertEqual((item2.calculate_cost()), 3.45)

    self.assertEqual((item1 > item2), True)
    self.assertEqual((item1 < item2), False)
    self.assertEqual((item1 == item2), False)
    self.assertEqual((item1 == item1), True)
    self.assertEqual((item1 != item2), True)
    self.assertEqual((item1 >= item2), True)
    self.assertEqual((item1 <= item2), False)

    self.assertEqual((obj1.order[0].calculate_cost()), 9.0)
    self.assertEqual((obj1.order[1].calculate_cost()), 3.45)

    self.assertEqual((obj1.order[0] > obj1.order[1]), True)
    self.assertEqual((obj1.order[0] < obj1.order[1]), False)

    # print(sorted(obj1.order))
    # print(obj1.order)
    # obj1.order = sorted(obj1.order)
    # print(obj1.order)

if __name__ == "__main__":
  mytest = DessertItemTest()
  mytest.setup()
  mytest.verify_lineage(DessertItem, Cookie, Candy, IceCream, Sundae)
  mytest.dessertinit(mytest.my_candy, mytest.my_candy2)
  mytest.dessertmethods(mytest.my_candy, mytest.my_candy2, mytest.my_sundae)
  mytest.ordermethods(mytest.my_order)
  mytest.test_str(mytest.my_candy, mytest.my_candy2, mytest.my_sundae)
  mytest.test_packaging(Cookie, Candy, IceCream, Sundae)
  mytest.test_paytype(mytest.my_order)
  mytest.test_sort(mytest.my_candy, mytest.my_candy2, mytest.my_order)
  print("done")




