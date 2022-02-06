# return n of random numbers(stop at 13)


import random

n = int(input('how many random numbers: '))

for _ in range(n):
    r = random.randint(10, 99)
    print(r, end=' ')
    if r == 13:
        print('\nfinish the program')
        break
else:
    print('\nfinish makeing random numbers')