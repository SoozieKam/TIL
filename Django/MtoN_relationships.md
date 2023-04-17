a# 11일차 Many to Many relationship -1

### 학습 목표

- Many to Many Field를 사용해서 다대다 관계를 설정할 수 있다.
- 다대다 관계에서 생성, 수정, 삭제 등의 작업을 어떻게 수행하는지 이해하고 활용할 수 있다.
- 다대다 관계에서 중개 모델이 필요한 이유와 활용법을 열거할 수 있다.

---

### 학습 내용

1.  Many to many relationship이란?
    <br> 양쪽 테이블 모두에서 다대다 관계인 경우
    <br> 예)

    - 병원에서 0개 이상의 게시글은 0명 이상의 회원과 관련된다.
    - 게시글은 회원으로부터 0개 이상의 좋아요를 받을 수 있고, 회원은 0개 이상의 게시글에 좋아요를 누를 수 있다.

2.  ManyToManyField's Arguments

    ```python
    # articles/models.py

    class Patient(models.Model):
        doctors = models.ManyToManyField(Doctor, related_name='patients', through='Reservation')
        name = models.TextField()

        def __str__(self):
            return f'{self.pk}번 환자 {self.name}'

    class Reservation(models.Model):
        doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
        patient = models.ForeinKey(Patient, on_delete=models.CASCADE)
        symptom = models.TextField()
        reserved_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f'{self.doctor.pk}번 의사의 {self.patient.pk}번 환자'
    ```

    둘 중 어느 class에 ManyToManyField를 넣어줘도 상관 없음. 역참조만 생각해주면 됨!

    # `역참조`란?

    외래키를 가지고 있지 않은 클래스를 통해서 외래키를 가지고 있는 클래스의 값을 가져오는 것이다.

    1. 'related_name'
       역참조시 사용하는 manager name을 변경해줌.

    변경 전) doctor.patient_set.all()
    변경 후) doctor.patients.all()

    2. 'through'
       중개 테이블을 직접 작성하는 경우 through 옵션을 사용해서 중개 테이블을 나타내는 Django 모델을 지정할 수 있다.

### 실습 주제

게시글 좋아요, 댓글 좋아요 기능 구현

### 실습 목표

- `N:M 관계`의 개념을 이해한다.
- 연관 관계가 있는 두 모델의 N:M 관계를 설정할 수 있다.
- QuerySet API를 활용해서 N:M 관계에 있는 두 모델을 다룰 수 있다.

### 성찰

- detail.html 템플릿에서 if를 여러 번 중첩해서 사용했는데, 분명 맞게 작성했는데 자꾸 에러가 난다. 예전부터 이랬다 장고 ..
