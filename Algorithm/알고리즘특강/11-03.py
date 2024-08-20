## 함수
import random
def selectSort(ary):
    n = len(ary)
    for i in range(0,n-1):
        minIdx = i
        for k in range(i+1, n):
            if (ary[minIdx] > ary[k]):
                minIdx = k
        ary[i], ary[minIdx] = ary[minIdx], ary[i]

    return ary






## 변수
dataAry = [random.randint(38,190) for _ in range(4)]

## 메인
print('정렬 전-->', dataAry)
dataAry = selectSort(dataAry)
print('정렬 후--->', dataAry)