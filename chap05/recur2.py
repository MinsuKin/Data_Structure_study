# genuine recursive

def recur(n: int) -> int:
    if n > 0:
        recur(n - 2)
        print(n)
        recur(n - 1)

x = int(input('num: '))

recur(x)