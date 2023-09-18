
class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation 
    
    def say_hello(self):
        print(f"Hello, my name is {self.name}")

class Superhero(Person):
    def __init__(self, name, age, occupation, superpower):
        super().__init__(name, age, occupation)
        self.superpower = superpower

    #this constructor and method is overriding the previous /method
    def say_hello(self):
        super().say_hello()
        print("I AM HERE")

    #this method is extending the class
    def fight(self):
        print("AHHHHHHHHHHHHHHHHHHH")

    def old_say_hello(self):
        super().say_hello()

hero = Superhero("Jessica Jones", 29, "private investigator", "stronk")
print(hero.name)
print(hero.superpower)

#print(help(Superhero))

#object is god 

'''

'''
class ClassA:
    pass
class ClassB(ClassA):
    pass 

objecta = ClassA()
objectb = ClassB()

print(isinstance(objecta, ClassA))#True
print(isinstance(objectb, ClassA))#True 
print(isinstance(objecta, ClassB))#False 

print(issubclass(ClassB, ClassA))#True
print(issubclass(ClassA, ClassB))#False

"""
"""

class Dinosaur:
  def __init__(self, size, weight):
    self.size = size
    self.weight = weight
    
class Carnivore:
  def __init__(self, diet):
    self.diet = diet
    
class Tyrannosaurus(Dinosaur, Carnivore):
  def __init__(self, size, weight, diet):
    Dinosaur.__init__(self, size, weight)
    Carnivore.__init__(self, diet)
    
tiny = Tyrannosaurus(12, 14, "whatever it wants")
#super does not work with multiple inheritance 
'''
#the .mro() method returns the order of inheritance for an object 
#it will always end in object bc object is god
obj= C()
obj.hello()

print(C.mro())
'''