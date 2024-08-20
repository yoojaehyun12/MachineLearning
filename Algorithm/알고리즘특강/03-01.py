## 함수 선언부
## 전역 변수부
katok = ['다현', '정연', '쯔위', '사나', '지효']

## 메인 코드부
print(katok)

#** 데이터 추가 (모모가 1회) --> 맨 뒤에
# 1단계 : 빈칸 추가
katok.append(None)
# 2단계 : 추가한 칸에 넣기
katok[5] = '모모'
print(katok)

#** 데이터 삽입 (미나가 40회 연속) --> 미나를 3등으로
# 1단계 : 빈칸 추가
katok.append(None)
# 2단계 : 마지막 친구부터 3등까지 한칸씩 뒤로 이동
katok[6] = katok[5]
katok[5] = None
katok[5] = katok[4]
katok[4] = None
katok[4] = katok[3]
katok[3] = None
# 3단계 : 삽입
katok[3] = '미나'
print(katok)

