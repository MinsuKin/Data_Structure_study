# greatest common divisor

def gcd(x: int, y: int) -> int:
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

if __name__ == '__main__':
    print('return gcd of two integers')
    x = int(input("first integer: "))
    y = int(input("second integer: "))

    print(f'gcd is {gcd(x, y)}.')