''' 
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

    def get_megapixels(self):
       return self._megapixels
    
    def set_megapixels(self, new_mega):
       self._megapixels = new_mega

    # def __private_method(self):
    #    return "I am a private method"

my_phone = Phone("phone", 256, 12)
print(my_phone._megapixels)
print(my_phone.get_megapixels) 
#we try to use gets and sets to change values to reduce unwanted side effects 
'''

class TestClass:
    def __init__(self, num1, num2):
        self._num1 = num1
        self._num2 = num2

    def get_num1(self):
        return self._num1

    def set_num1(self, new_num):
        self._num1 = new_num

    def get_num2(self):
        return self._num2

    def set_num2(self, new_num):
        self._num2 = new_num 

my_obj = TestClass(2, 3)

class Person:
    def __init__(self, name):
        self._name = name

    #getters
    def name(self):
        return self._name
    
    def get_name(self):
        return self._name 
    
    name = property(get_name) 

    @property
    def name(self):
        return self._name 
    
    @name.setter #decorator has the name of the function in it 
    def name(self):
        #data validation in set
        if type(new_name) != str:
            raise TypeError("Name must be a string")
        self._name(self, new_name)
        self._name = new_name

    
c = Person("BLYAT")
#getters
print(c._name) #calls the variable itself
print(c.name()) #calls the instance method 
print(c.name) #ZEN- calls the method with the property decorator
#setter
c.name = ("Fedya") #calls the setter, they can have the same name 
