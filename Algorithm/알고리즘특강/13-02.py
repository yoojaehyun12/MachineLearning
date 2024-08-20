## 함수
import random
def binSearch(ary, fdata):
    global count
    pos = -1
    start = 0
    end = len(ary) - 1
    while (start <= end):
        mid = (start + end)// 2
        if (ary[mid] == fdata):
            pos = mid
            break
        elif (ary[mid] < fdata):
            start = mid + 1
        else:
            end = mid - 1
    return pos




## 변수
dataAry = [random.randint(0,99999999999999) for _ in range(1000000)]
findData = random.choice(dataAry)
dataAry.sort()

# 메인
count = 0
print('배열:', dataAry[:20])
position = binSearch(dataAry, findData)
if position != -1 :
    print(findData, '는', position, '위치에 있음(', count,'번)')
else:
    print(findData, '는 없어요')
