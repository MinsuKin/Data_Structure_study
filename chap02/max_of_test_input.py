# find max value from list and print

from max import max_of

print('find max value')
print('"End" will make you exit from the program')

number = 0
x =[]

while True:
    s = input(f'put the value of x[{number}]: ')
    if s == 'End':
        break
    x.append(int(s))
    number += 1

print(f'you put {number} values')
print(f'max value is {max_of(x)}')