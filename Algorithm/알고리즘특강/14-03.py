## 함수
def factorial(num):
    if (num==1) :
        return 1

    return num * factorial(num-1)



## 메인
print('\n5!=', factorial(5))