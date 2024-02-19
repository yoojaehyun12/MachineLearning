# OOP

1. 객체(Object)

> python 에서 모든 것은 객체이다.
> 모든 객체는 타입, 속성, 조작법 을 가진다.

- 타입(type) : 값이 숫자나 문자에 따라 답이 달라지기 때문에, 이러한 값의 종류를 데이터타입(data type), 혹은 타입(type) 이라고 함.
    > 인스턴스(instance) 
    - 특정 객체가 어떤 클래스의 객체인지 관계를 중점으로 표현할 때 사용

- 속성(attribute) : 나이, 이름, 성별, 군필여부, 롤 티어 등등 고유 데이터

- 조작법(method) : 걷기, 뛰기, 자기 등등 동작 행위

---
## Class 와 Instance
> `class` : 객체들의 분류를 정의할 떄 쓰이는 키워드

>`instance` : 객체의 실제 예시


**Class 활용법**
```
class <클래스이름>:
    <statement>

class ClassName:
    statement
```

**Instance 활용법** 
```
# 인스턴스 = 클래스()

person1 = Person()
```

**Method 활용법**
```
class Person:
    # 메서드(method)
    def talk(self):  # 인자로 self를 정의해봅시다  
        print('안녕')
```

생성자(constructor) 매서드 정의 및 활용법

- 인스터스 객체가 생성될 때 호출되는 함수. 반드시`__init__`이라는 이름으로 정의

```
class MyClass:
    def __init__(self):
        print('생성될 때 자동으로 호출되는 메서드입니다.')
```

소멸자(destructor) 매서드 정의 및 활용법

- 인스턴스 객체가 소멸되기 직전에 호출되는 함수. 반드시 `__del__`이라는 이름으르 정의

```
def __del__(self):
    print('소멸될 때 자동으로 호출되는 메서드입니다.')
```

속성(attribute) 정의 및 활용법

- 특정 데이터 타입의 객체들이 가지게 될 상태/데이터를 의미


```
class Person:
    def __init__(self, name):
        self.name = name
        
    def talk(self):
        print(f'안녕, 나는 {self.name}')
```


정리하자면!

객체(Object)

- 객체는 자신 고유의 속성(attribute) 을 가지며 클래스에서 정의한 행위(behavior) 를 수행

클래스(Class)

- 공통된 속성(attribute)과 행위(behavior)를 정의한 것으로 객체지향 프로그램의 기본적인 사용자 정의 데이터형(user-defined data type)

인스턴스(Instance)

- 특정 class로부터 생성된 해당 클래스의 실체/예시(instance)
속성(Attribute)

- 클래스/인스턴스가 가지는 속성(값/데이터)

메서드(Method)

- 클래스/인스턴스에 적용 가능한 조작법(method) & 클래스/인스턴스가 할 수 있는 행위(함수)