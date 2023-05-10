# Relations 정참조와 역참조 

### 학습 내용

1.  정참조  
    <br> 내가 참조하는 
    <br> 예)

    - 병원에서 0개 이상의 게시글은 0명 이상의 회원과 관련된다.
    - 게시글은 회원으로부터 0개 이상의 좋아요를 받을 수 있고, 회원은 0개 이상의 게시글에 좋아요를 누를 수 있다.

2.  ManyToManyField's Arguments

    ```python
    # articles/models.py
