# sum of 1 to n

print('return sum of 1 to n')
n = int(input('put value of n : '))

sum = 0
i = 1

while i <= n:
    sum += i
    i += 1

print(f'{sum} is sum of 1 to {n}')