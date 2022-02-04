# sum of 1 to n (for)

print('return sum of 1 to n')
n = int(input('put value of n : '))

sum = 0
for i in range(1, n + 1):
    sum += i

print(f'{sum} is sum of 1 to {n}')