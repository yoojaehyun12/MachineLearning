# 제어문

## 조건문(Conditional Statement)
- `if` 문은 반드시 참/거짓을 판단할 수 있는 조건과 함께 사용해야 함.

### `if` 조건문의 구성
#### 활용법

- 문법
```
if <조건문>:
    <코드 블럭>
else:
    <코드 블럭>
```
- 예시
```
if a > 0: # 조건이 참일 때
    print('양수입니다.')
else: # 조건이 거짓일 때
    print('음수입니다.')
```
    
- `elif` 들어올수도 있고, `else`는 선택적으로 사용해도 된다.
#### 주의사항
- 반드시 __들여쓰기__ 를 유의해야 함.

### `while` 반복문

- `while` 문은 조건식이 참 인 경우 반복적으로 코드 실행 시킨다.

- 문법
```
while <조건식>:
    <코드블럭>
```
- 예시
```
while True:
    print('조건식이 참일 때 까지')
    print('계속 반복')
```

#### 주의 사항
- 반드시 종료조건을 설정해야 한다.

### `for` 문

`for` 문은 시퀀스(string, tuple, list, range)를 포함한 순회가능한 객체(iterable)의 요소들을 순회합니다

- 문법
```
for <임시변수> in <순희가능한 데이터>
    <코드블럭>
```
- 예시
```
for menu in ['김밥', '햄버거', '피자', '라면']:
    print(menu)
```

### 반복제어 (`break`, `continue`, `for-else`)

- `break`
    - 반복문을 종료(for 나 while 문을 빠져나올수 있다.)

- `continue`
    - continue 이후 코드를 수행하지 않고 다음 요소부터 계속 반복 수행.

- `for-else`

- `pass`


좀 더 자세히 알고 싶으면 [위키독스-제어문](https://wikidocs.net/20) 클릭 !!

