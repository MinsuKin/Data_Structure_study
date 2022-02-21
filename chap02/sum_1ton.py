# sum of 1 to n

def sum_1ton(n):
    s = 0
    while n > 0:
        s += n
        n -= 1
    return s

x = int(input('put value of x: '))
print(f'sum of 1 to {x} is {sum_1ton(x)}.')