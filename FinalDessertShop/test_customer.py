from dessertshop import Customer, DessertShop
from desserts import Order, Candy, Cookie, IceCream, Sundae
# from sqlalchemy import Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

#copied exactly from desssertshop
# Base = declarative_base()
# engine = create_engine('sqlite:///customer.db')
# Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)


def make_order():
    order = Order()
    order.add(Candy('Candy Corn', 1.5, 0.25))
    order.add(Sundae('Vanilla', 3, 0.69, 'Hot Fudge', 1.29))
    order.add(Cookie('Oatmeal Raisin', 2, 3.45))
    return order

def test_customer(customer1, customer2, customer3, shop):
    customer1.add2history()
    shop.print_shop_history()

    customer2.add2history()
    shop.print_shop_history()

    customer3.add2history()
    shop.print_shop_history()

'''
('Veronica', 'Candy Corn\nVanilla\nOatmeal Raisin\nTotal number of items in order: 3\n, PayType: CASH')

('Veronica', 1)

('Veronica', 'Candy Corn\nVanilla\nOatmeal Raisin\nTotal number of items in order: 3\n, PayType: CASH')
('Emmalee', 'Candy Corn\nVanilla\nOatmeal Raisin\nTotal number of items in order: 3\n, PayType: CASH')

('Veronica', 1)
('Emmalee', 1)

('Veronica', 'Candy Corn\nVanilla\nOatmeal Raisin\nTotal number of items in order: 3\n, PayType: CASH; Candy Corn\nVanilla\nOatmeal Raisin\nTotal number of items in order: 3\n, PayType: CASH')
('Emmalee', 'Candy Corn\nVanilla\nOatmeal Raisin\nTotal number of items in order: 3\n, PayType: CASH')

('Veronica', 2)
('Emmalee', 1)
'''


def test_unique_id(customer1, customer2, customer3, shop):
  assert(type(shop.customer_db)== dict)

  shop.generate_id(customer1.name)
  assert((shop.id_db) == {'Veronica': 1001})
  assert((shop.id_db[customer1.name]) == 1001)
  shop.generate_id(customer2.name)
  assert((shop.id_db) == {'Veronica': 1001, 'Emmalee': 1002})
  assert((shop.id_db[customer2.name]) == 1002)
  shop.generate_id(customer3.name)
  assert((shop.id_db) == {'Veronica': 1001, 'Emmalee': 1002})
  assert((shop.id_db[customer3.name]) == 1001)


if __name__ == "__main__":
  shop = DessertShop()
  customer1 = Customer("Veronica", make_order(), shop)
  customer2 = Customer("Emmalee", make_order(), shop)
  customer3 = Customer("Veronica", make_order(), shop)
  # test_customer(customer1, customer2, customer3, shop)
  test_unique_id(customer1, customer2, customer3, shop)
  print("done")

