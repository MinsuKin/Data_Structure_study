# Chained hash test

from enum import Enum
from chained_hash import ChainedHash

Menu = Enum('Menu', ['add', 'delete', 'search', 'dump', 'exit'])

def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '   ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)

hash = ChainedHash(13)

while True:
    menu = select_menu()

    if menu == Menu.add:
        key = int(input('put a key to add: '))
        val = input('put a value to add: ')
        if not hash.add(key, val):
            print('add failed')

    elif menu == Menu.delete:
        key = int(input('put a key to delete: '))
        if not hash.remove(key):
            print('delete failed')

    elif menu == Menu.search:
        key = int(input('put a key to search: '))
        t = hash.search(key)
        if t is not None:
            print(f'the value of searched key is {t}')
        else:
            print('there is no data to search')

    elif menu == Menu.dump:
        hash.dump()

    else:
        break

