"""
Dessert Shop!!
"""

class Coffee:
    dish = "mug"
    price = 3.00

    _sizes = [12, 16, 24, 32]
    _bases = ["pour over", "esspresso", "chai"]
    _syrups = ["pumpkin", "caramel", "toffee", "raspberry", "vanilla"]
    _milks = ["Whole", "2%", "Almond", "Oat"]

    def __init__(self, size, temp, base, syrup=None, milk=None, whipped_cream=False):
        self._size = size
        self._temp = temp
        self._base = base
        self._syrup = syrup
        self._milk = milk
        self._whipped_cream = whipped_cream


class Bread:
    dish = "large plate"
    price = 4.00

    _bread_types = ["zucchini", "pumpkin", "banana", "sour dough", "wheat", "white"]

    def __init__(self, bread_type):
        self._bread_type = bread_type

class Toast(Bread):
    price = 4.50
    _toppings = ["butter", "brown sugar butter", "avocado", "cream cheese", "jam"]

    def __init__(self, bread_type, topping):
        super().__init__(bread_type)
        self._topping = topping

class Cookie:
    dish = "small plate"
    price = 2.50 

    _types = ["snickerdoodle", "chocolate chip", "sugar", "seasonal"]

    def __init__(self, type):
       self._type = type 

class Order:
    _total_price = 0.00
    _total_dishes = 0