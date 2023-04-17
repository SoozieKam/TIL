a# 7일차 ORM w.view -2

### 학습 목표

- QuerySet API를 사용해 데이터를 수정하고 삭제하는 방법을 익힌다.
- Django View 함수를 사용해서 데이터베이스에서 가져온 데이터를 처리할 수 있다.
- Django ORM과 View함수를 결합해서 웹 어플리케이션의 데이터를 저장하고 렌더링할 수 있다.
- HTTP request methods를 사용해 클라이언트가 서버로 보내는 요청의 종류를 나타낼 수 있다.
- HTTP response status codes를 사용해 서버가 클라이언트에 반환하는 응답의 상태를 올바르게 나타낼 수 있다.
- Django view 함수를 사용해서 데이터베이스에서 가져온 데이터를 삭제 및 수정할 수 있다.

---

### 학습 내용

1.  ORM
    <br> 1. ORM UPDATE

    ```python
    article = Article.objects.get(pk=1)
    article.title = 'bye'
    article.save()
    ```

    이 방법이 제일 괜찮음. 한번에 데이터를 수정하는 방법도 있는데 (create 메서드 사용) 그러면 제약조건이 반영되지 않을 수 있어서 save 전 확인하는 단계를 거치는 게 좋음!

    2. ORM DELETE

    ```python
    article.delete()
    ```

2.  Django - ORM with view<br> 1. app URLs 분할 및 연결
    <br> 앱이 많아지면 이렇게 구별하는 게 좋음

            1. project/urls.py에서 <br>
            `from django.urls import path, include` 추가
            2. project/urls.py의 urlpatterns 리스트 안에 아래 내용 추가 <br>
            `path('articles/', include('articles.urls')),`
            3. 앱 폴더 안에 urls.py 만들기
            4. app/urls.py 에 아래 내용 추가 <br>
            `from . import views`
            5. app/urls.py 에 `app_name` 추가
            6. app/urls.py의 urlpatterns 리스트 안에 url 링크 추가
            --> name='' 따로 지정해주는 게 좋음

        2. View 작성
            1. app/views.py 에서 아래 내용 import <br>
            `from .models import 클래스 이름`
            2. 함수 작성
                - `render`와 `redirect`
                    1. render
                    2. redirect : 인자에 작성된 주소로 다시 요청을 보냄

        3. Template 작성

        4. READ (조회)
            1. app/views.py
                ```python
                def detail(request, todo_pk):
                    todo_1 = Todo.objects.get(pk=todo_pk)
                    context = {
                        'todo' : todo_1,
                    }
                    return render(request, 'todos/detail/html', context)
                ```
                변수 이름 조심해야 함 !

            2. template
            view함수의 context 딕셔너리의 key 값을 template에서 사용. 이런 식으로 ! `{{todo.title}}`

        5. CREATE (생성)
            1. view 함수 2개 필요
                - new 함수 (사용자의 입력 받는 페이지를 렌더링)
                - create 함수 (사용자가 입력한 데이터를 DB에 저장)

            2. template
                1. new 로직
                    -`form`, `label`, `input` 태그 주로 사용
                2. create 로직
                    - template 작성은 필요 없음
                    - `HTTP request methods` : 데이터에 원하는 행동을 요청하는 것
                        1.`GET': 특정 리소스를 조회. Query String  형식으로 데이터가 보여짐
                        - view 함수에서 사용 예
                        todo.title = request.GET.get('title')

                        2. `POST`: 특정 리소스에 변경사항을 만듦. HTTP Body에 데이터가 담김.
                        - view 함수에서 사용 예
                        todo.title = request.POST.get('title')

                        ** POST 쓸 때는 해당 부분 템플릿 아래줄에  `csrf_token 태그` 넣어줘야 함 (이유는.. 보안 때문. 추후 추가)

        6. DELETE (삭제)
        7. UPDATE (수정)
            1. view 함수 2개 필요 (당연!)
                1. edit 함수 : 사용자의 입력을 받는 페이지 렌더링
                2. update 함수 : 사용자가 입력한 데이터를 받아 DB에 저장
            2. 주의사항
                - 수정 시 이전 데이터가 출력되도록 해야 함!
                template의 input 값의 value를 이전 데이터로 설정해야 함
                예)
                ```html
                <input type="text" name="title" id="title" value="{{todo.title}}">
                ```
                - 수정 버튼을 누르면 해당 글의 edit 페이지로 넘어가야 하니 하이퍼링크 작성에 pk값이 들어가야 함
                예)
                ```html
                <a href="{% url 'todos_app:edit' todo.pk %}>EDIT</a>
                ```

### 실습 주제

생성, 조회, 수정, 삭제가 가능한 Todo 웹 서비스 개발

### 실습 목표

- Model 정보가 주어졌을 때 Django Model을 설계할 수 있다.
- `CRUD 기능`이 구현된 웹 서비스를 개발할 수 있다.

### 성찰

- ORM의 CRUD 를 다 배우니 하나의 게시판을 만들 수 있어서 성취감이 들었다.
- detail 페이지에 들어갈 때 NoReverseMatch 에러가 계속 나서 한참 헤맸는데, delete 페이지로 가는 form 에서 오타가 나서 그런 거였다 ...ㅎ
  form 의 action이 {% url 'todos_app:delete' todo.pk %} 가 되어야 하는데 todo.delete 인가 여튼 이상하게 되어 있었음 ^-^
- 보통 noReverseMatch 나오면 페이지 이동할 때 문제가 생긴 것이다! url과 view 함수의 변수 이름 잘 보자.
- form, label 등 태그의 type 값을 어떻게 넣어주냐에 따라 베리에이션이 많아서 이 부분을 더 공부해 봐야겠다.
