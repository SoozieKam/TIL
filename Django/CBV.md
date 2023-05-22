## CBV (Class-Based View)

1. CBV란?
    - 클래스를 이용한 뷰 
    - django.views.generic.View 에서 as_view() 클래스 메서드를 제공하고, 모든 CBV는 이 클래스를 직간접적으로 상속받아 사용함

2. CBV의 장점
    - 코드의 재사용으로 인한 개발 생산성 증진
    - HTTP 메서드에 따른 처리 코드 작성 시 if 함수 대신 메소드 명을 사용하여 코드 구조가 깔끔함 

3. 제너릭 뷰
    1) Base View: 다른 제너릭 뷰의 부모 클래스가 되는 기본 제너릭 뷰
        - View: 최상위 부모 제너릭 뷰 클래스 
        - TemplateView: 주어진 템플릿으로 render 
        - RedirectView: 주어진 url로 redirect 

    2) Generic Display View: 객체의 목록 또는 하나의 객체를 출력하는 뷰 
        - DetailView: 조건에 맞는 하나의 객체 출력 
        - ListView: 조건에 맞는 객체 목록 출력 

    3) Generic Edit View: 폼을 통해 C, U, D 기능을 제공하는 뷰 
        - FormView: 폼이 주어지면 해당 폼을 출력 
        - CreateView: 객체 생성 폼 출력
        - UpdateView: 기존 객체 수정하는 폼 출력 
        - DeleteView: 기존 객체 삭제하는 폼 출력 

4. 구현 예시 
    : 뷰 + 모델폼 

    ``` python
    from django.views.generic import CreateView, UpdateView, DetailView
    from braces.views import LoginRequiredMixin
    from .models import Flavor

    class FlavorCreateView(LoginRequiredMixin, CreateView):
        model = Flavor
        fields = ('title', 'slug', 'scoops_remaining')

    class FlavorUpdateView(LoginRequiredMixin, UpdateView):
        model = Flavor
        fields = ('title', 'slug', 'scoops_remaining')

    class FlavorDetailView(DetailView):
        model = Flavor

    ```

5. 제너릭 뷰 오버라이딩 
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
        - `def get_context_data(**kwargs): 뷰에서 템플릿 파일에 넘겨주는 context 데이터 추가 및 변경을 위해 오버라이딩 
        -  `def form_valid(form)`

    3) 구현 예시 
        ``` python
        
        from django.views.generic import ListView, DetailView
        
        from .models import Question

        class IndexView(ListView):
        template_name = 'cbvpolls/index.html'
        context_object_name = 'latest_question_list'

        def get_queryset(self):
            return Question.objects.order_by('-pub_date')[:5]


        class DetailView(DetailView):
            model = Question
            template_name = 'cbvpolls/detail.html'


        class ResultsView(DetailView):
            model = Question
            template_name = 'cbvpolls/results.html'
        ```