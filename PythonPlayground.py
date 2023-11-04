#Decorators in Python
#Unit 9

# function, method, class decorator 
# decorators add things to a block

# Generators

# list comprehenion []
squared_list = [ x**2 for x in range(10)]
for item in squared_list:
    print(item)

# generator expression ()
squared_gen = ( x**2 for x in range(10))
for item in squared_gen:
    print(item)

# result is the same but
# generators create insances of gen and once its done being used, it is gone,
# not remembered in the main memory

def even_numbers(n):
    for i in range(n):
        if i %2 == 0:
            yield i 

# yield is like return but for generators
# it allows you to have a sequence of returned values, therefore is compatible with the for loop
#generators

even_gen = even_numbers(10)
for num in even_gen:
    print(num)

# filter
even_gen = (x for x in range(20) if x%2 == 0)
for num in even_gen:
    print(num)

# chaining generators
def squares(n):
    for i in range(n):
        yield i**2

def even_squares(n):
    for square in squares(n):
        if sqaure % 2 ==0:
            yield square 

even_square_gen = even_squares(10)
for num in even square_gen:
    print(num)

# generating infinite sequences
def fibonacci(i):
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

#yield is an output that can be recursively called 
fib = fibonacci()
for i in range(10):
    print(next(fib))