# sort objects in mutablesequence reversely

from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n // 2):
        a[i], a[n - i - 1] = a[n - i - 1], a[i]

if __name__ == '__main__':
    print('sort objects in mutablesequence reversely')
    nx = int(input('how many objects? : '))
    x = [None] * nx

    for i in range(nx):
        x[i] = int(input(f'put the value of x[{i}]: '))

    reverse_array(x)

    print('sorted objects in mutablesequence reversely')
    for i in range(nx):
        print(f'x[{i}] = {x[i]}')
