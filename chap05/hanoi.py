# tower of hanoi

def move(no: int, x: int, y: int) -> None:
    
    if no > 1:
        move(no - 1, x, 6 - x - y)

    print(f'move disk[{no}] from tower{x} to tower{y}.')

    if no > 1:
        move(no - 1, 6 - x - y, y)


print('tower of hanoi')
n = int(input('how many disks?: '))

move(n, 1, 3)