# get three integers and find the biggest integer.

print('find the biggest integer from three of them.')
a = int(input('put a value of an int a.:'))
b = int(input('put a value of an int b.:'))
c = int(input('put a value of an int c.:'))

# sequential structure
max = a
if b > max: max = b # select structure
if c > max: max = c

print(f'the biggest integer is {max}')