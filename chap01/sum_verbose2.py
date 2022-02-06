# sum of int a to b (for) 2
"""separate code and remove if structure to enhance the code"""

print('return sum of a to b')
a = int(input('put value of a : '))
b = int(input('put value of b : '))

if a > b:
    a, b = b, a

sum = 0
for i in range(a, b + 1):
    print(f'{i} + ', end='')
    sum += i

print(f'{b} = ', end='')
sum += b

print(sum)