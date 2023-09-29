#polymorphism 
class TestClass:
  def sum(self, a = None, b = None, c = None):
    if a is not None and b is not None and c is not None:
      return a + b + c
    elif a is not None and b is not None:
      return a + b
    elif a is not None:
      return a
    else:
      return 0
    
obj = TestClass()
# print(obj.sum())
# print(obj.sum(1))
# print(obj.sum(1, 2))
# print(obj.sum(1, 2, 3))

'''Polymorphism is when you can use the same call to do multiple things,
 ie + that can add and concatenate. method overriding does this'''

#method overloading- using the same method to do different things
'''
class TestClass:
  def sum(self, a, b, c):
    return a + b + c
  
  def sum(self, a, b):
    return a + b
  
obj = TestClass()
print(obj.sum(1, 2, 3))
#returns an error message because python uses the last declared method
'''
class TestClass:
  def sum(self, a, b, c=0):
    return a + b + c

obj = TestClass()
# print(obj.sum(1,2)),
# print(obj.sum(1, 2, 3))
#works because c is optional
#if I put c as None the first one throws an error but the second doesn't 

'''overloading- this case uses an if else block to decide which thing to do 
from the same method.'''
#teacher example:
class TestClass:
  def sum(self, a = None, b = None, c = None):
    if a is not None and b is not None and c is not None:
      return a + b + c
    elif a is not None and b is not None:
      return a + b
    elif a is not None:
      return a
    else:
      return 0
    
obj = TestClass()
print(obj.sum())
print(obj.sum(1))
print(obj.sum(1, 2))
print(obj.sum(1, 2, 3))

#operator overloading

#duck typing 
class Baseball:
  def __init__(self, power):
    self._power = power

  def hit(self):
    if self._power >= 10:
      return "Home Run"
    else:
      return "weak"
    

class Song:
  def __init__(self, title, author):
    self._title = title
    self._author = author

  def hit(self):
    if self._author == "Fall Out Boy":
      return "YEAHHHHHHHH"
    elif self._title == "Paradise":
      return "Yeahhhhhh!"
    else:
      return "nahhhh"
    
def print_hit(obj):
  try:
    print(obj.hit())
  except AttributeError as e:
    print(e) 

#crashing your code is the highest severity of bug that there is
#it's better to print an error message than to crash the system

#possible becuase both baseball and song are objects

my_player = Baseball(12)
my_song = Song("Paradise", "Rude A")

print_hit(my_player)
print_hit(my_song)

