# print numbers (de morgan's laws)

print('put numbers of 10 to 99')

while True:
    no = int(input('put number: '))
    # if no >= 10 and no <= 99:
    # if 10 <= no <= 99:
    if not(no < 10 or no > 99):
        break

print(f'the number you put is {no}')