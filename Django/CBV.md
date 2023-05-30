## CBV (Class-Based View)

1. CBV란?
    - 클래스를 이용한 뷰 
    - django.views.generic.View 에서 as_view() 클래스 메서드를 제공하고, 모든 CBV는 이 클래스를 직간접적으로 상속받아 사용함

2. CBV의 특징
    - 코드의 재사용으로 인한 개발 생산성 증진
    - HTTP 메서드에 따른 처리 코드 작성 시 if 함수 대신 메소드 명을 사용하여 코드 구조가 깔끔함 

    - CBV vs FBV (Function-based view)
    <img src="https://miro.medium.com/v2/resize:fit:828/format:webp/1*1NgVsYmmLCiwXUy-uE0VLA.jpeg">

    - FBV
    <br>장점: 구현이 간단함, 읽기 편함, 직관적인 코드, 데코레이터 사용이 간단함
    
    <br>단점: 코드를 확장하거나 재사용하기 어려움, 조건문으로 HTTP 메소드 구분

    - CBV
    <br>장점: 내장된 뷰를 사용해서 코드를 확장하거나 재사용하기 쉬움, mixin(다중 상속) 같은 객체지향 기술을 사용할 수 있음, 분리된 메소드로 HTTP 메소드 구분 가능

    <br>단점: 읽기 힘듦, 직관적이지 않은 코드 (부모 클래스/mixin에 숨어있는 코드들이 많기 떄문) 뷰 데코레이터를 사용하려면 따로 import를 하거나 메소드를 오버라이드 해야 함


3. 제너릭 뷰
    - 웹 어플리케이션에서 일반적으로 사용되는 기능을 구현하기 위해 도입됨 (예: 폼 처리, 페이징, 새로운 객체 생성 등)
    - https://docs.djangoproject.com/en/3.2/ref/class-based-views/ 이 링크를 참고하여 작성 

    1) Base View: 다른 제너릭 뷰의 부모 클래스가 되는 기본 제너릭 뷰
        - View: 최상위 부모 제너릭 뷰 클래스 
        - TemplateView: 주어진 템플릿으로 render. 정적인 페이지 구현 시에 쓰임. 
        - RedirectView: 주어진 url로 redirect 

    2) Generic Display View: 객체의 목록 또는 하나의 객체를 출력하는 뷰 
        - DetailView: 조건에 맞는 하나의 객체 출력 
        - ListView: 조건에 맞는 객체 목록 출력 

    3) Generic Edit View: 폼을 통해 C, R, U, D 기능을 제공하는 뷰 
        - FormView: 폼이 주어지면 해당 폼을 출력 
        - CreateView: 객체 생성 폼 출력
        - UpdateView: 기존 객체 수정하는 폼 출력 
        - DeleteView: 기존 객체 삭제하는 폼 출력 

    4) 그 외: 
        - Date-Based Views
        - ArchiveIndexView
        - YearArchiveView
        - MonthArchiveView
        - WeekArchiveView
        - DayArchiveView
        - TodayArchiveView
        - DateDetailView

4. 제너릭 뷰 오버라이딩 
    : 오버라이딩이란? 부모 클래스로부터 상속받은 메서드의 내용을 자손 클래스에 맞게 변경하는 것

    1) 속성 변수 오버라이딩
        - `model`: Base View를 제외하고 모든 제너릭 뷰에서 사용 
        -  `queryset`: Base View를 제외하고 모든 제너릭 뷰에서 사용. `queryset`을 사용하면 `model` 속성은 무시됨.
        - `template_name`: 템플릿 파일명을 문자열로 지정
        - `context_object_name`: 뷰에서 템플릿 파일에 전달하는 context 변수명 지정 
        - `form_class`: FormView, CreateView, UpdateView에서 폼을 만드는 데 사용할 클래스 지정
        - `success_url`: 폼에 대한 처리가 성공한 후 redirect할 url 주소 

    2) 메서드 오버라이딩
        - `def get_queryset()`
        - `def get_context_data(**kwargs)`: 뷰에서 템플릿 파일에 넘겨주는 context 데이터 추가 및 변경을 위해 오버라이딩 
        -  `def form_valid(form)`


5. 구현 예시 
    1) 기본적인 형태 

    - views.py
    ```python
    from django.views import View

    class ContactView(View):
        def get(self, request):
            # Code block for GET request

        def post(self, request):
            # Code block for POST request
    ```

    - urls.py
    ```python
    urlpatterns = [
        path('contact/', ContactView.as_view(), name='contact'),
    ]
    ```

    2) List View (+ Q search)
    : 검색 쿼리에 맞는 결과를 가져오기 위해 ListView에서 지원하는 기본 queryset 수정 
    => ListView의 get_queryset() 메서드 오버라이드! 

    ```python
    from django.views.generic import ListView

    from .models import Flavor

    class FlavorListView(ListView):
        model = Flavor

        def get_queryset(self):
            # 부모 get_queryset으로부터 queryset을 petch 
            queryset = super().get_queryset()
            
            # GET 파라미터를 받는다.
            q = self.request.GET.get("q")
            if q:
                # 필터된 queryset을 반환
                return queryset.filter(title__icontains=q)
            # 기본 queryset 반환
            return queryset
    ```


6. 제너릭 뷰의 확장
    : Generic view를 사용하면 개발 속도를 크게 높일 수 있으나, 대부분의 프로젝트에서는 제너릭 뷰만으로는 더이상 충분하지 않은 순간이 온다. 사실 새로운 Django 개발자들이 가장 많이 하는 질문은 더 다양한 상황을 다루는 generic view를 어떻게 만들 수 있는가이다. 
    => 뷰를 generic view의 서브클래스로 구현하는 것이 어렵다면 사용자 정의 클래스 기반 혹은 함수 기반 뷰를 사용해 필요한 코드를 직접 작성하는 것이 더 효율적일 수 있다!


7. 기타 
    1) super() : 하위 클래스에서 상위 클래스의 메서드를 오버라이드할 때 쓰는 함수. 

    - super().메서드명(인자) 형태: 현재 클래스의 상위 클래스에서 해당 메서드를 호출합니다. 이를 통해 상위 클래스의 동작을 유지하면서 추가적인 동작을 구현할 수 있습니다.

    - super(현재클래스, self).메서드명(인자) 형태: 현재 클래스가 다중 상속을 받을 때 특정 상위 클래스의 메서드를 호출합니다. super() 함수의 첫 번째 인자로 현재 클래스를 전달하고, 두 번째 인자로 self를 전달하여 호출합니다.

    ```python
    class ParentClass:
        def __init__(self, name):
            self.name = name

        def greet(self):
            print(f"Hello, I'm {self.name}!")

    class ChildClass(ParentClass):
        def __init__(self, name, age):
            super().__init__(name)
            self.age = age

        def greet(self):
            super().greet()
            print(f"I'm {self.age} years old.")

    child = ChildClass("Alice", 10)
    child.greet()
    ```
