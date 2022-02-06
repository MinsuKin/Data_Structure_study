# sum of int a to b (for) 1

print('return sum of a to b')
a = int(input('put value of a : '))
b = int(input('put value of b : '))

if a > b:
    a, b = b, a

sum = 0
for i in range(a, b + 1):
    if i < b:
        print(f'{i} + ', end='')
    else:
        print(f'{i} = ', end='')
    sum += i

print(sum)