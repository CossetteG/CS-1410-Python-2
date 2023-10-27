class NegativeNumberError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def check(self, num):
        if num < 0:
            raise NegativeNumberError("no negs allowed")
        else:
            return num 

checker = NegativeNumberError()
# help(Exception)

# a= checker.check(-25)

def square_root(num):
    # if num < 0:
    #     raise NegativeNumberError(";alskjf")
    # num = checker.check(num)
    return checker.check(num)**.5

try:
    num = float(input("Enter a number: "))
    result = square_root(num)
except NegativeNumberError as e:
    print("bogwater")
    print(e)
else:
    print(f"The square root of {num} is {result}")



total = 0
for i in range(100):
    s = i + 1
    total += s
    # print(total)