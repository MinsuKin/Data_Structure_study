# print + and - repeatedly 2
"""separate code and remove if structure to enhance the code"""

print('print + and - repeatedly')
n = int(input('print how many?: '))

for _ in range(n // 2):
    print('+-', end='')

if n % 2:
    print('+', end='')

print()