# convert decimal to 2~36

def card_conv(x: int, r: int) -> str:
    d = ''
    dchar = '012345678ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while x > 0:
        d += dchar[x % r]
        x //= r

    return d[::-1]

if __name__ == '__main__':
    print('convert decimal to n')

    while True:
        while True :
            no = int(input('put number: '))
            if no > 0:
                break

        while True :
            cd = int(input('convert to which n?: '))
            if 2 <= cd <= 36:
                break
        
        print(f'{cd} is {card_conv(no, cd)}.')

        retry = input("convert again?(Y/N): ")
        if retry in {'N', 'n'}:
            break