# "is" vs. "=="
a = 1000
b = 1000

a == b  # True
a is b  # False

id(a) == id(b)  # False
