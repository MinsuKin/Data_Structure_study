# sum of 1 to n(only for positive numbers)

print('return sum of 1 to n')

while True:
    n = int(input('put value of n : '))
    if n > 0:
        break

sum = 0
i = 1

for i in range(1, n + 1):
    sum += i
    i += i

print(f'{sum} is sum of 1 to {n}')