# python 기초

## 1. 주석 (Comment)

- 한 줄 주석은 `#` 표현

- 여러 줄의 주석은
    1. 한 줄 씩 `#` 으로 사용해서 표현하거나,

    1. `"""` 또는 `'''` 사용함

## 2. 코드 라인

- 파이썬 코드는 '1줄에 1문장' 원칙

- 문장(statement)은 파이썬이 실행 가능(executable)한 최소한의 코드 단위

- 기본적으로 파이썬에서는 ; 작성 X
    
    **한 줄로 표기할때는 ;을 작성하여 표기 할 수 있다** 

- 줄을 여러 줄 작성할 때는 역슬래시(\) 사용한다

- [] {} () 는 \ 없이도 가능

## 3. 변수(Variable)

### 3.1 `=`: 할당 연산자(Assignment Operator)

- 변수는 `=` 을 통해 할당

- 해당 데이터 타입을 확인하기 위해 type() 활용

- 해당 값의 메모리 주소를 확인하기 위해 id() 활용

- 같거나 다른 값을 동시에 할당 할 수 있다.

```
#
x = 1 y = 2
# 코드를 활용하여 x = 2 y = 1
x = x + y >>  x = 3 y = 1
y = x - y >>  x = 3 y = 2
x = x - y >> x = 1 y = 2
```

### 3.2 식별자(identifiers)

파이썬에서 식별자는 변수, 함수, 모듈, 클래스 등을 식별하는데 사용되는 이름(name) 이다

 - 식별자의 이름은 영문알파벳(대문자와 소문자), 언더바(_), 숫자로 구성

 - 첫 글자에 숫자 불가능

 - 길이에 제한 없음

 - 대소문자 구별

 - 아래의 키워드는 사용 불가(굳이 안외도됨)
```False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield```

- 내장함수나 모듈등이 이름으로도 만들면 안됨

## 4. 데이터 타입(Data Type)

- 숫자(Number)

- 문자(String)

- 참/거짓(boolean)

### 4.1 int(정수, ingteger)

모든 정수는 `int` 로 표현

### 4.2 float (부동소수점, 실수)

실수는 `float` 로 표현

### 4.3 문자열(String)

- 문자열은 `(')`, `(")` 을 활용하여 표현 가능

    - ' : '"큰" 따옴표를 담을 수 있음'

    - " : " '작은' 따옴표를 담을 수 있음"

    - ```/""" : '''안녕''' , """안녕"""

- 단, 문자열을 묶을 때 동일한 문장부호를 활용해야한다!

---

#### 이스케이스 시퀀스

```
\n	줄 바꿈
\t	탭
\r	캐리지리턴
\0	널(Null)
\	\
\'	단일인용부호(')
\"	이중인용부호(")
```

### 참/거짓(Boolean) 타입

파이썬에는 `True`와`False`로 이뤄진 `bool` 타입이 있다.

#### None 타입

값이 없음을 표현

## 연산자

**산술 연산자**
```
+	덧셈
-	뺄셈
*	곱셈
/	나눗셈
//	몫
%	나머지(modulo)
**	거듭제곱
```

**비교 연산자**

```
<	미만
<=	이하
>	초과
>=	이상
==	같음
!=	같지않음
is	객체 아이덴티티
is not	부정된 객체 아이덴티티

```

**논리연산자**

```
a and b	a와 b 모두 True시만 True
a or b	a 와 b 모두 False시만 False
not a	True -> False, False -> True
```

**복합연산자**
```
a += b	a = a + b
a -= b	a = a - b
a *= b	a = a * b
a /= b	a = a / b
a //= b	a = a // b
a %= b	a = a % b
a **= b	a = a ** b
```

    