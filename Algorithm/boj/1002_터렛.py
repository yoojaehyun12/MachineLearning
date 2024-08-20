# 두 원의 위치 관계(r1, r2 :반지름 두 점과의 거리 : d )
# 1 두 점에서 만나는 경우 r1 - r2 < d
# 2 한 점에서 만나는 경우 r1 + r2 = d
# 3 만나지 않는 경우 r1 - r2 > d
import math

a = int(input())
for _ in range(a):
    b = input().split(' ')

    x1 = int(b[0])
    y1 = int(b[1])
    r1 = int(b[2])
    x2 = int(b[3])
    y2 = int(b[4])
    r2 = int(b[5])

## 함수


## 변수

    d = math.sqrt((x2-x1)**2 + (y2-y1)**2) # math.sqrt 는 루트!

## 메인
    if x1 == x2 and y1 == y2 and r1 == r2:
       print(-1)
    else:
       if abs(r2 - r1) == d or r2 + r1 == d:
              print(1)
       elif abs(r2 - r1) > d or r2 + r1 < d:
               print(0)
       elif r2 + r1 > d:
              print(2)

