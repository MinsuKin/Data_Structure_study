# find max value from random numbered list and print

import random
from max import max_of

print('find max value')
num = int(input('how many random numbers: '))
lo = int(input('minimum value: '))
hi = int(input('maximum value: '))
x =[None] * num

for i in range(num):
    x[i] = random.randint(lo, hi)

print(f'{(x)}')
print(f'max value is {max_of(x)}')