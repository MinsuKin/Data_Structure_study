# find max value in sequence

# Any: any data type
# Sequence: any sequence type(list, tuple, str, bytes, bytearray)
from typing import Any, Sequence

# data type of parameter a is Sequence
# return value is Any which is any data type(int, float)
def max_of(a: Sequence) -> Any:
    # use """~""" for a fuction annotation and it states that this is mutable sequence
    """시퀀스형 a 원소의 최댓값을 반환"""
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum

# python reusable module(max.py를 직접 시작한 경우에만 name과 main이 일치하여 if문이 실행됨)
if __name__ == '__main__':
    print('find max value')
    num = int(input('how many objects: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'put the value of x[{i}]: '))

    print(f'the max value is {max_of(x)}.')