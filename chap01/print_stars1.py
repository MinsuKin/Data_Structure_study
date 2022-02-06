# print * n times, but newline after w times

print('print *')
n = int(input('print how many *?: '))
w = int(input('newline after how many *?: '))

for i in range(n):
    print('*', end='')
    if i % w == w - 1:
        print()

if n % w:
    print()