

class Dinosaur:
  def __init__(self, size, weight):
    self.size = size
    self.weight = weight
    
class Carnivore:
  def __init__(self, diet):
    self.diet = diet
    
#bottom to top, left to right 
class Tyrannosaurus(Dinosaur, Carnivore):
  def __init__(self, size, weight, diet):
    Dinosaur.__init__(self, size, weight)
    Carnivore.__init__(self, diet)
    #pass the Tyrannosaurus self as a paramenter in the dinosaur and carnivore constructors 

    
tiny = Tyrannosaurus(12, 14, "whatever it wants")
#print(tiny.diet)


class A:
  def hello(self):
    print("Hello from A")

class B:
  def hello(self):
    print("Hello from B")

  def break_my_computer(self):
    print("Crazy? I was crazy once. They locked me in a room. A rubber room. A rubber room with rats. The rats make me crazy")
    B().break_my_computer()

class C(A, B):
  #overriding
  def hello(self):
    B().hello()
    #you do need the parentheses after B
    #overrides the hello() in A because A is the first inherited hello() function

  #extending
  def bonjour(self):
    print("Bonjour")

#multiple inheritance is debatable on whether on or not its a good design strategy
#some languages support it and some don't
obj = C()
obj.hello()
#super does not work with multiple inheritance because Python doesnt know what its referring to

#cohesion refers to how related data is to eachother
#classes increase cohesion
#multiple inheritences lower cohesion

#New Module: Encapsulation, Getters and Setters
#methods and data are encapsulated in their class - can be described by venn diagrams
#Python usually has no data restrictions - accessible from anywhere. Most languages don't allow this
#public = no restrictions 
#private = restricted 
class Phone:
    def __init__(self, model, megapixels, storage):
      self.model = model
      self._megapixels = megapixels
      #the underscore is a conventional way to notate a private variable in Python
      #it will not throw an error if you try to access it publicly tho
      self.__storage = storage
      #the dender makes it look like a private thing, it's just invisible to the outside 
      #for any dender the compiler adds a class name to it

    def helper(self):
      #use self.storage

my_phone = Phone("iPhone", 12)
print(my_phone.model)
print(my_phone._megapixels) 

# print(my_phone.__storage)
#throws an error that says it doesn't exist. 
      
print(my_phone.__dict__)
#^useful function to show all the stuff declared in a class 






