# 함수 (function)

1. 정의(`define`) 과 호출(call)


2. in & out

3. out(`return`)
    - 리턴값은 단 하나의 값
    - `return` 키워드를 만나면 그 자리에서 함수 종료
    - `return` 키워드가 없으면 코드 끝나고 `None` 을 반환
    - `return` 만 있고 그 뒤에 아무말 없으면 그 자리에서 종료하고 `None` 을 반환
    - `print` 는 리턴 없는 `None` 함수

4. in(parameter > 매개변수 / argument > 전달 인자)
    - 있을수도 있고 없을 수도 있다
    - 기본적으로 위치(자리)에 맞춰 들어간다
    - 정의할 때는 기본값(default value) 세팅 가능
    - 실행할 때는 위치 안맞추고 키워드로 실행 가능
    - 여러개를 묶어서 받을 수 있다
        
        i. 값들만 받으면 `fun(1, 2, 3)` ==> def func(*args) 처럼 튜플로 묶어서 받을 수 있다.

        ii. 값과 이름을 같이 받으면 `func(a=1, b=2, c=3)` ==> `def func(**kwargs)` 처럼 dictionart로 묶어서 받을 수 있다.

