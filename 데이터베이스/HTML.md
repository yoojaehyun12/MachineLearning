# HTML

## 00_intro

- vscode 안에 있는 확장자에서 __open in browser__ 설치하면, 
보다 편리하게 html 문서 작성 할 수 있다.

- `ctrl + /` : 주석 활용

- `open in browser`를 설치하면 `! + tab키`를 누르면 자동으로 html 양식이 만들어 진다

    ```
    <!DOCTYPE html>
    <html lang="en">
        # Head > Metadata
    <head>
        # 글자 인코딩
        <meta charset="UTF-8">
        # 문서의 제목
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        # Body > 실제 문서 표시됨    
    </body>
    </html>
    ```

## 01_heading

- html 파일의 제목 쓰는 법 : `<title>제목쓰기</title>`

- 마크다운 처럼 제목별(크기) 로 나눌 수 있다.
    
```
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>01_Heading</title>
</head>
<body>
    <h1>가장 큰 제목</h1>    
    <h2>하위 제목1</h2>
    <h3>333333333</h3>
    <h4>444444444</h4>
    <h5>555555555</h5>
    <h6>6666666666</h6>
    <h2>하위 제목2</h2>
    <h2>하위 제목3</h2>

</body>
</html>
```

- <h2>하위 제목2</h2> 을 여러 번 사용 하고 싶을 때 : h2*n(n=1,2,3...)

## 02_content

- `문단(paragraph)` : 한 문단 별로 나눠 줌 => <p>아무 문장</p>

- 할 말 없을 때 문단 채우는 용도(lorem) : lo 쓰면 자동완성으로 loram 이라고 뜨는데 엔터누르면 알아서 써줌.

- `Sementic (의미를 갖는) / Non Sementic (의미가 없는)`
    - Sementic (의미를 갖는) : <strong>강조1</strong>, <em>강조2</em>

    - Non Sementic (의미가 없는) : <b>굵게</b>, <i>이텔릭</i> 

- `html에서 코드 작성 시` : <p>code</p> 라고 하면 안됨 >> <pre>code</pre> 라고 해야됨.

## 03_link

- 기본 링크 : a 치고 tab 키 누르면 자동완성으로 <a href=""></a> 됨.
    ```
        <p>
            <!-- 기본 링크 -->
            구글로 가려면 <a href="https://google.com">Google</a>을 클릭하세요
        </p>
    ```

- 새 탭에서 열기 : 기본링크처럼 누른 상태에서 <a href="" target="_blank"></a> 치면 되는데 이것 또한 t 누르면 알아서 나와주고 _ 누르면 알아서 _blank 나옴!
    ```
        <p>
            <a href="https://naver.com" target="_blank">Naver</a> 새탭에서 열립니다.
        </p>
    ```

- 비어있는 링크 : 말 그대로 비어있음
    ```
        <p>
            <a href="">목적지 미정</a>이지만 우선 링크 생성
        </p>
    ```

## 04_list

- Ordered List(순서 있는 리스트)
    
    ```
    <ol>
        <li>html 학습</li>
        <li>복습</li>
        <li>마크다운 정리</li>
        <li>내일 내용 예습</li>

            # li 안에 ol 가능!
            <ol>
                <li>CSS</li>
            </ol>
    </ol>
    ```

- Unordered List(순서 없는 리스트)
    
    ```
    <ul>
        <li>html 학습</li>
        <li>복습</li>
        <li>마크다운 정리</li>
        <li>내일 내용 예습</li>
            <ul>
                <li>CSS에 대해서 예습</li>
            </ul>
    </ul>
    ```

## 05_table



