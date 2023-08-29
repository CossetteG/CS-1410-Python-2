''' a+plus_b.py
    
    = + and += can behave differently with mutable data structures, like lists.
    Compare the behavior of lines 9 vs. 20 below.
'''

a = [1, 2]
also_a = a
b = [3]
a += b
print(a)
print(also_a)

del a
del b
del also_a

a = [1, 2]
also_a = a
b = [3]
a = a + b
print(a)
print(also_a)
