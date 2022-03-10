# take n of values and save the last n of values

n = int(input('how many int you want to save: '))
a = [None] * n

cnt = 0
while True:
    a[cnt % n] = int(input((f'put the {cnt + 1}th value.: ')))
    cnt += 1

    retry = input(f'do you want to keep going?(Y/N): ')
    if retry in {'N', 'n'}:
        break

i = cnt - n
if i < 0 : i = 0

while i < cnt:
    print(f'{i + 1}th = {a[i % n]}')
    i += 1