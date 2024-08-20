# Spark_Streaming

## Window Function
Window Function 이란 데이터의 특정한 범위를 설정하고, 그 범위 내에서 집계 함수 등 적용하는 함수를 의미한다

- 스파크 스트리밍에서 기본적으로 time-based-window만을 사용한다
- > 즉 다른 window를 적용하면 오류가 나게 된다

### 대표적인 윈도우 설정
-  `Sliding Window` : 가장 많이 사용되는 window

    - 슬라이딩 윈도우는 고정된 크기의 윈도우를 가지며, 윈도우 사이에 겹치는 구간이 존재 

    ![sliding window](<캡처이미지/sliding window.png>)

- `Tumbling Window`
슬라이딩 윈도우와 마찬가지로 텀블링 윈도우는 고정된 크기의 윈도우를 갖는다. 하지만 윈도우 간의 겹치는 구간이 없다

    ![tumbling window](<캡처이미지/tumbling window.png>)

- `Session Window` : 이벤트 성 window

    - 세션 윈도우는 슬라이딩, 텀블링 윈도우와는 다르게 윈도우의 크기가 가변적이다.
    - 처음 윈도우가 생성된 후 레코드/이벤트가 설정한 gap duration 내에 들어오면 윈도우가 확장된다
        - 만약, gap duration 내에 event가 들어오지 않는다면 이 윈도우는 끝나고, 새로운 이벤트가 들어오면 새로운 window가 생성된다
    
    ![session window](<캡처이미지/session window.png>)

## Event time windows
- 이벤트 타임 윈도우는 이벤트 타임 기준으로 입력되는 레코드 처리 방식
- 레코드 혹은 이벤트가 실제로 생성된 시점
    - 즉, 스파크 스트리밍은 어플리케이션에 레코드가 들어온 시간을 의미하지 않는다

- 따라서, 이벤트 타임에 대한 정보는 입력 레코드에 컬럼으로 반드시 제공되어야 한다(`timestamp 로 찍기`)