# get three ints and return median 2

def med3(a, b, c):
    if (b >= a and c <= a) or (b <= a and c >= a):
        return a
    elif (a > b and c < b) or (a < b and c > b):
        return b
    return c

print('get median from 3 ints')
a = int(input('put value for int a : '))
b = int(input('put value for int b : '))
c = int(input('put value for int c : '))

print(f'median is {med3(a, b, c)}')