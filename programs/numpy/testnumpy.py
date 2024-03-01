import numpy as np

print("Python list operations:"); 
a = [1, 2, 3]
b = [4, 5, 6]

print("a+b:", a+b);

try:
  print(a*b)
except TypeError:
  print("a*b has no meaning for Python lists")

print()
print("numpy array operation:")

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("a+b:", a+b); 
print("a*b:", a*b); 


