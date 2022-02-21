# '==' and 'is' are different

## '==' uses eqality

### '==' to know if values of both objects are the same

## 'is' uses identity

### 'is' to know if values and ids of both objects are the same


# 내포 표기 생성

### 리스트 안에서 for, if 문을 사용하여 새로운 리스트를 생성한다

```numbers = [1,2,3,4,5]

twise = [
    num * 2 
    for num in numbers 
        if num % 2 == 1
    ]
print(twise)

#[2, 6, 10]```