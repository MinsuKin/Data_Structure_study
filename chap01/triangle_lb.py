# print triangle

n = int(input('put height: '))

for i in range(n):
    for j in range(i + 1):
        print('*', end='')
    print()