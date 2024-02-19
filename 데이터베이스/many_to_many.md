<!-- 240118 요약

User - Article - Comment 모델의 관계
Profile 페이지
권한(작성자 == 요청보낸사용자)에 따라서 동작 구분
HTML 에서 UI 들 변경(사용자 클릭, 프로필페이지에서 작성글/댓글, 보기)

M:N 관계의 핵심 (연결테이블)
M:N 관계로 표현해야하는 개념들이 어떤게 있는지
models.py 코드들 -->

# Many_To_Many

1. `User(클라이언트) - Article(게시글) - Comment(댓글) 모델의 관계`

   - User : Article = 1 : N => 한 명의 클라이언트가 여러 게시글을 쓸 수 있 듯이, 이러한 관계를 1:N 이라고 설명할 수 있다.

   - User : Comment = 1: N 이다

        즉, Article : Comment = M : N 으로 무수히 많은 게시글을 쓸 수 있으면, 댓글 또한 많이 쓸 수 있다. 이러한 관계를 `Many_To_Many` 라고 한다.

2. `Profile 페이지`
 
    - 프로필 페이지에서는 사용자(username), 사용자가 작성한 글들, 사용자가 달아놓은 댓글들이 있을 건데, 만드는 법은

    ```
        accounts(우리가 만든 앱) > views.py

        from django.contrib.auth import get_user_model

        def profile(request, username):
            User = get_user_model() 
            # get_user_model 은 장고에서 지원한 모델이므로 import 해서 쓰면 됨. # 프로필 만들 때 유용함.
            user = get_object_or_404(User, username=username)
            return render(request, 'accounts/profile.html', {
                'user' : user
            })

    ```

  3. `권한(작성자 == 요청보낸사용자)에 따라서 동작 구분`

        ```
            # 지금 요청 보낸 너가 글쓴이가 아니라면
            if request.user != article.user:
                # 당장 돌아가 원래있던 화면으로
                return redirect('board:article_index')

            # html에서도 한 줄 코드 써줘야 함.
            # 지금 요청한 사용자가 게시글의 사용자가 맞다면 수정/삭제 가능!
            {%if article.user == request.user%}
            <div>
            (수정/삭제 관련된 코드 들어가있음)
            <div/>
            {%endif%}

        
        ```

        위에 주석이 어떤 상황이냐면, user1이 만든 게시글, 댓글들이 있는데 
        
        개발자들이 아무 코드도 안해놓으면 갑자가 user2라는 사람이 와서 user1꺼 수정/삭제 할 수 있자나??

        그래서, 지금 요청 보낸게 글쓴이가 아니라면 넌 자격 없으니 돌아가라 이 말인거야.


4. `HTML 에서 UI 들 변경(사용자 클릭, 프로필페이지에서 작성글/댓글, 보기)`

        ```
        이전 코드 >>
        {{comment.user}}){{ comment.content }}

        바꾼 코드 >>
        <a href="{% url "accounts:profile" comment.user %}">
        {{comment.user}})
        </a> {{ comment.content }}

        이전 코드 >>
        작성자: {{article.user}}
        
        바꾼 코드 >>
        작성자: <a href="{% url "accounts:profile" article.user %}">
        {{article.user}}
        </a>

        # a링크만 걸어둔거!

        ```


    
    
    <!-- M:N 관계의 핵심 (연결테이블)
    M:N 관계로 표현해야하는 개념들이 어떤게 있는지
    models.py 코드들 --> 




5. `게시글에서 좋아요/싫어요 누르는거 만드는 법`

    1. `urls.py` 에서 url 부터 만들어야 한다.
        ```
        # board/1/like/
        path('<int:article_pk>/like/', views.article_like, name='article_like')
        ``` 
    2. `view` 함수를 만들어 리턴 해주자.
        ```
        @require_POST
        @login_required
        def article_like(request, article_pk):
            article = get_object_or_404(Article, pk=article_pk)
            user = request.user
        
            # user in article.like_users.all() => 파이썬이 일함
            # user article.like_users.filter(pk=user.pk).exists() => DB 가 일함

            # 좋아요를 이미 누른 상태라면,
            if article.like_users.filter(pk=user.pk).exists():
                article.like_users.remove(user)
            # 누르지 않았다면,
            else:
                article.like_users.add(user)

            return redirect('board:article_detail', article.pk)
        
        ```

    3. `HTML` 문서 작성(제일 만만한 detail 문서에서 작성 할 예정)

        ```
        <!-- 좋아요 UI -->
        # 요청한 사용자가 인증(로그인)되있다면?
        {%if request.user.is_authenticated%} 
    
        <div>
        <form action="{% url "board:article_like" article.pk %}" method="POST">
            {% csrf_token %}
            <button>
            {% if is_like %}💗{% else %}🤍{% endif %}
            좋아요{{article.like_users.count}}
            </button>
        </form>
        </div>
        {%endif%}
        
        
        
        ```



