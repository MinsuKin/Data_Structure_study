# get three ints and return median

def med3(a, b, c):
    if a >= b:
        if b >= c:
            return b
        elif a <= c:
            return a
        else:
            return c
    elif a > c:
        return a
    elif a > c:
        return c
    else:
        return b

print('get median from 3 ints')
a = int(input('put value for int a : '))
b = int(input('put value for int b : '))
c = int(input('put value for int c : '))

print(f'median is {med3(a, b, c)}')