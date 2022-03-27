# tower of hanoi 2

def move(no, x, y):
    print(f'move disk[{no}] from tower{x} to tower{y}.')

def hanoi(num, start, nd):
    hanoi_sub(num, start, nd, 2)

def hanoi_sub(num, start, nd, other):
    if num == 1:
        move(1, start, nd)

    else:
        hanoi_sub(num - 1, start, other, nd)
        move(num, start, nd)
        hanoi_sub(num - 1, other, nd, start)

hanoi(3, 1, 3)