# sum of a to b (for)

print('return sum of a to b')
a = int(input('put value of a : '))
b = int(input('put value of b : '))

if a > b:
    a, b = b, a # sort a and b in ascending order

sum = 0
for i in range(a, b + 1):
    sum += i

print(f'{sum} is sum of {a} to {b}')