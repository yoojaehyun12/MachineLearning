## 함수
def countDown(num):
    if (num==0) :
        print('발사!')
    else:
        print(num)
        countDown(num-1)

## 메인
countDown(10)