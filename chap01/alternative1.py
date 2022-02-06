# print + and - repeatedly

print('print + and - repeatedly')
n = int(input('print how many?: '))

for i in range(n):
    if i % 2:
        print('-', end='')
    else:
        print('+', end='')

print()