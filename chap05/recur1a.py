# not recursively (remoce tail recursion)

def recur(n: int) -> int:
    while n > 0:
        recur(n - 1)
        print(n)
        n = n -2

x = int(input('num: '))

recur(x)