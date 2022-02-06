# print * n times, but newline after w times
"""separate code and remove if structure to enhance the code"""

print('print *')
n = int(input('print how many *?: '))
w = int(input('newline after how many *?: '))

for _ in range(n // w):
    print('*' * w)

rest = n % w
if rest:
    print('*' * rest)