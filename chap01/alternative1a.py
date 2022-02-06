# print + and - repeatedly (change for statement)

print('print + and - repeatedly')
n = int(input('print how many?: '))

for i in range(1, n + 1):
    if i % 2:
        print('+', end='')
    else:
        print('-', end='')

print()