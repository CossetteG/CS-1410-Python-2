from desserts import Cookie, Candy, IceCream, Sundae, Order
from receipt import make_receipt, make_data
#my reciept was made but then it didn't show in codio idk if it will show 
#for you but if you download it you can see it

# from sqlalchemy import Column, Integer, String, PickleType
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# import sqlalchemy.types as types



def main():
    dessert_order = Order()
    dessert_order.add(Candy("Candy Corn", 1.5, .25))
    dessert_order.add(Candy("Gummy Bears", .25, .35))
    dessert_order.add(Cookie("Chocolate Chip", 6, 3.99))
    dessert_order.add(IceCream("Pistachio", 2, .79))
    dessert_order.add(Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29))
    dessert_order.add(Cookie("Oatmeal Raisin", 2, 3.45))

    for order in dessert_order():
      print(order)
    make_receipt(make_data(dessert_order), "receipt.pdf")

# Base = declarative_base()
# engine = create_engine('sqlite:///customer.db')
# Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)

# class AnOrder(types.TypeDecorator):
#   types.TypeDecorator.load_dialect_impl(PickleType)
#   cache_ok = False

# class Customers(Base):
#   __tablename__ = 'users'

#   name = Column(String, primary_key=True)
#   order = Column(String)
 
#   def __repr__(self):
#     return self.name + ": " + self.order


class Customer:
    id = 0

    def __init__(self, name, order, shop):
        self.name = name
        self.orderstr = str(order)
        self.shop = shop

    def add2history(self):
        if self.name in self.shop.customer_db:
          self.shop.customer_db[self.name] += "; " + self.orderstr
          self.shop.customer_count_db[self.name] +=1
        else:
          self.shop.customer_db[self.name] = self.orderstr
          self.shop.customer_count_db[self.name] = 1


        
'''
    def add2history(self):
        session = Session()
        customers = [] #session.query(Customers).all()
        # return customers
        
        if self.name in customers:
          curr_customer = session.query(Customers).filter(Customers.name == self.name).first()
          curr_customer.order += "; " + self.orderstr
        else:
          print("checkpoint1")
          customr = Customers(name=self.name, order=self.orderstr)
          session.add(customr)
        session.commit()
        
        session.close()

    def print_customers(self):
      session = Session()
      # customers = session.query(Customers).all()
      # print(name + ": " + str(ordr) for order in customers)
      # print(customers)
      session.close()
'''
	
def main_():
    shop = DessertShop() 
    order = Order()
    '''
    order.add(Candy('Candy Corn', 1.5, 0.25))
    order.add(Candy('Gummy Bears', 0.25, 0.35))
    order.add(Cookie('Chocolate Chip', 6, 3.99))
    order.add(IceCream('Pistachio', 2, 0.79))
    order.add(Sundae('Vanilla', 3, 0.69, 'Hot Fudge', 1.29))
    order.add(Cookie('Oatmeal Raisin', 2, 3.45))
    '''
    # boolean done = false
    done: bool = False
    # build the prompt string once
    prompt = '\n'.join([ '\n',
            '1: Candy',
            '2: Cookie',            
            '3: Ice Cream',
            '4: Sundae',
            '\nWhat would you like to add to the order? (1-4, Enter for done): '
      ])

    while not done:
      choice = input(prompt)
      match choice:
        case '':
          name = input("Can I get a name for the order? ")
          customer = Customer(name, order, shop)
          customer.add2history()
          count = shop.customer_count_db[name]
          shop.generate_id(name)
          id = shop.id_db[name]

          pay = shop.user_prompt_payment()
          order.set_pay_type(pay)

          order.order = sorted(order.order)
          make_receipt(make_data(order, name, count, id), "receipt.pdf")

          anotha = input("Would you like to make another order(y for yes)?")
          if anotha == 'y':
            order = Order()
          else:
            done = True
        case '1':            
          item = shop.user_prompt_candy()
          order.add(item)
          print(f'{item.name} has been added to your order.')
        case '2':            
          item = shop.user_prompt_cookie()
          order.add(item)
          print(f'{item.name} has been added to your order.')
        case '3':            
          item = shop.user_prompt_icecream()
          order.add(item)
          print(f'{item.name} has been added to your order.')
        case '4':            
          item = shop.user_prompt_sundae()
          order.add(item)
          print(f'{item.name} has been added to your order.')
        case _:            
          print('Invalid response:  Please enter a choice from the menu (1-4) or Enter')
    print()

    

    

class numError(Exception):
  def check(self, num:int or float, mode:"int" or "float"):
    if mode == "int":
      if type(num) != int or num <= 0:
        raise numError(f"{num} is not a positive integer")
      else:
        return num
    elif mode == "float":
      if type(num) != float or num <= 0.00:
        raise numError(f"{num} is not a positive float")
      elif num*100%1 != 0.0:
        if num*10*10%1 == 0.0:
          print("you have number that python doesn't work super well with btw")
          return num
        else:
          raise numError(f"Too many decimals in this number: {num}")
      else:
        return num
    else:
      raise numError("Your mode was input incorrectly")

class DessertShop:
  checker = numError()
  y = (n + 1000 for n in range(1, 100))

  customer_db = {} #:dict[str, Customer]
  customer_count_db = {}
  id_db = {}

  def print_shop_history(self):
    for item in list(self.customer_db.items()):
      print(item)
    print()

    for item in list(self.customer_count_db.items()):
      print(item)
    print()

  def generate_id(self, name):
      if name in self.id_db:
        pass
      else:
        self.id_db[name] = next(self.y)

      return self.id_db[name]


  def user_prompt_candy(self):
    asking = True
    success1 = False
    success2 = False
    reprompt = "Try giving me that candy again"
    while asking: 
      self.candy_name = input("Tell me the name of that candy: ")
      try:
        self.candy_weight = self.checker.check(float(input("And how many pounds of that are you getting? ")), "float")
      except(numError) as e:
        print(e)
        print(reprompt)
        self.candy_weight = 0.0
        self.candy_price = 0.0
      except(ValueError):
        print("Numerical input only")
        print(reprompt)
        self.candy_weight = 0.0
        self.candy_price = 0.0
      else:
        success1 = True
        try:
          self.candy_price = self.checker.check(float(input("And what's the price of that candy? ")), "float")
        except(numError) as e:
          print(e)
          print(reprompt)
          self.candy_price = 0.0
        except(ValueError):
          print("Numerical input only")
          print(reprompt)
          self.candy_price = 0.0
        else:
          success2 = True
      finally:  
        if success1 and success2:
          return Candy(self.candy_name, self.candy_weight, self.candy_price)
          break
        

  def user_prompt_cookie(self):
    asking = True
    success1 = False
    success2 = False
    reprompt = "Try giving me that cookie again"
    while asking: 
      self.cookie_name = input("Tell me the name of that cookie: ")
      try:
        self.cookie_amount = self.checker.check(int(input("And how many cookies are you getting? ")), "int")
      except(numError) as e:
        print(e)
        print(reprompt)
        self.cookie_amount = 0.0
        self.cookie_price = 0.0
      except(ValueError):
        print("Numerical input only")
        print(reprompt)
        self.cookie_amount = 0.0
        self.cookie_price = 0.0
      else:
        success1 = True
        try:
          self.cookie_price = self.checker.check(float(input("And what's the price per dozen of that cookie? ")), "float")
        except(numError) as e:
          print(e)
          print(reprompt)
          self.cookie_price = 0.0
        except(ValueError):
          print("Numerical input only")
          print(reprompt)
          self.cookie_price = 0.0
        else:
          success2 = True
      finally:  
        if success1 and success2:
          return Cookie(self.cookie_name, self.cookie_amount, self.cookie_price)

  def user_prompt_icecream(self, mode=False):
    asking = True
    success1 = False
    success2 = False
    reprompt = "Try giving me that ice cream again"
    while asking:
      self.icecream_name = input("Which ice cream would you like? ")
      try:
        self.icecream_scoops = self.checker.check(int(input("And how many scoops of that are you getting? ")), "int")
      except(numError) as e:
        print(e)
        print("No scoops or price added to this item")
        self.icecream_scoops = 0.0
        self.icecream_price = 0.0
      except(ValueError):
        print("Numerical input only")
        self.icecream_scoops = 0.0
        self.icecream_price = 0.0
      else:
        success1 = True
        try:
          self.icecream_price = self.checker.check(float(input("And what's the price of that icecream? ")), "float")
        except(numError) as e:
          print(e)
          print("No price added to this item")
          self.icecream_price = 0.0
        except(ValueError):
          print("Numerical input only")
          self.icecream_price = 0.0
        else:
          success2 = True
      finally:  
        if mode and success1 and success2:
          return (self.icecream_name, self.icecream_scoops, self.icecream_price)
        elif success1 and success2:
          return IceCream(self.icecream_name, self.icecream_scoops, self.icecream_price)

  def user_prompt_sundae(self):
    asking = True
    success3 = False
    reprompt = "Try giving me that cookie again"
    while asking:
      self.sundae_name, self.sundae_scoops, self.sundae_price = self.user_prompt_icecream(True)
      self.sundae_top = input("And what topping would you like with that? ")

      try:
        self.sun_top_price = self.checker.check(float(input("And what's the price of that topping? ")), "float")
      except(numError) as e:
        print(e)
        print("No topping or topping price added to this item")
        self.sundae_price = 0.0
      except(ValueError):
        print("Numerical input only")
        self.sundae_price = 0.0
      else:
        success3 = True
      finally:
        if success3:
          return Sundae(self.sundae_name, self.sundae_scoops, self.sundae_price, self.sundae_top, self.sun_top_price)
          break
  
  def user_prompt_payment(self):
    asking = True 
    reprompt = "Please enter a number for one of the options"
    while asking:
      paynum = input("How are you paying today? Enter 1 for cash, 2 for card, 3 for phone. ")
      if paynum == "1":
        return "CASH"
        break
      elif paynum == "2":
        return "CARD"
        break
      elif paynum == "3":
        return "PHONE"
        break
      else:
        print(reprompt)



if __name__ == "__main__":
	main()
  # my_shop = DessertShop()
  # candyy = my_shop.user_prompt_candy()
  # cookiee = my_shop.user_prompt_cookie() 
  # creamie = my_shop.user_prompt_icecream()
  # sundie = my_shop.user_prompt_sundae()
  # print(candyy, cookiee, creamie, sundie)

