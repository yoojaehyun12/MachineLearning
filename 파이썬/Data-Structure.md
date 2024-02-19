# 데이터 구조(Data Structure)

## 1. 문자열(string)

> 변경 할 수 없고(immutable), 순서가 있고(orderde), 순회 가능(iterable)


### 1.1 조회/탐색

- `.find(x)` : x의 **첫 번째 위치**를 반환. 없으면 `-1` 반환

- `.index(x)` : x의 **첫 번째 위치**를 반환. 없으면 오류 뜸

- `.replace(old, new[, count])` : 바꿀 대상 글자를 새로운 글자로 바꿔서 반환.
count를 지정하면 해당 갯수만큼 시행
- `.strip` : 특정 문자 지정시, 양쪽 제거나 왼쪽만 제거(lstrip), 오른쪽만 제거(rstrip), 지정하지 않을 시 (양쪽)공백 제거
- `.split` : 문자열을 특정한 단위로 나누어 리스트로 반환

- `separator.join`(iterable) : 특정한 문자열로 만들어 변환.
```
word = '배고파'
words = ['안녕', 'hello']
'!'.join(word) >> '배!고!파'
' '.join(words) >> '안녕 hello'
```
- `.capitalize()` : 앞글자를 대문자로 만들어 반환합니다.

- `.title()` : 어포스트로피나 공백 이후를 대문자로 만들어 반환합니다.
- `.upper()` : 모두 대문자로 만들어 반환합니다.

- `lower()` : 모두 소문자로 만들어 반환합니다.

- `swapcase()` : 대 <-> 소문자로 변경하여 반환합니다.

## 리스트(list)

> 변경 가능(mutable), 순서 있고(ordered), 순회 가능(iterable)

### 값 추가 및 삭제

- `.append()` : 리스트에 값 추가

- `.extend()` : 리스트에 iterable(list, range, tuple, string**[주의]**) 값을 붙일 수가 있습니다.
- `.insert(i, x)` : 정해진 위치 `i` 값 추가

- `remove(x)` : 리스트에서 값이 x인 것 삭제

- `.pop(i)` : 정해진 위치 `i` 에 있는 값 삭제하며,그 항목은 반환
`i` 가 지정되지 않을시 마지막 항목 삭제 및 되돌려줌.
- `.clear()` : 리스트의 모든 항목 삭제

- `.index(x)` : x 값을 찾아 해당 index 값을 반환.

- `.count(x)` : 원하는 값의 개수 변환.

- `.sort()` : 정렬한다.
내장함수`sorted()` 와 다르게 **원본list를 변형**, `None` 을 리턴한다.
```
import random
lotto = random.sample(range(1, 46), 6)
print(lotto, sorted(lotto))

# .sort => 원본 바꿈.return없음
# .sorted => 원본 안바꿈. return 있음

[23, 16, 6, 43, 9, 34] [6, 9, 16, 23, 34, 43]
```

- `.reverse()` : 반대로 뒤집는다(정렬X)

- `리스트 복사방법`
    - slice 연산자 사용(:)
    - .copy() 활용