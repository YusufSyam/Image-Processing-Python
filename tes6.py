from numpy import arange
from numpy import array
import numpy as np

(a, b, c)= arange(0,3)

for i in (a, b, c):
    print(i)

a= {'c': array([[0, 1]]),
    'b': array([[2, 1]])}

itemso= a['c']
keys = [print(itemso.flatten()) for k, v in a.items() if np.all(v) == np.all(itemso)]

print(f'{keys}')

print('-------------------')
print(array([[2, 1]]).flatten())