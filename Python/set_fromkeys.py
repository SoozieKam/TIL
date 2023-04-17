# 프로그래머스 '중복된 문자 제거'

""" 문자열 my_string이 매개변수로 주어질 때, my_string에서 
중복된 문자를 제거하고 하나의 문자만 남긴 문자열을 return하도록 
solution 함수를 완성해주세요. 

# 테스트 케이스 
my_string = 'people'
return 값 = 'peol' """


def solution(my_string):
    return ''.join(list(dict.fromkeys(my_string)))


""" 딕셔너리로 바꾼 후 다시 리스트 > 문자열 순서로 바꿔주면 
중복이 제거된다. Python 3.7 이상부터는 딕셔너리가 key값을 넣는 순서를 기억하기 때문! 
 """

# 아래처럼 set으로 바꿔버리면 순서가 뒤죽박죽이 된다.
# return ''.join(set(my_string))

# 파이썬 dict.fromkeys(seq, value) 메서드
""" 기본적으로는 딕셔너리 생성 메서드이다.
"""
# 사용 예시

seq = ('name', 'age', 'sex')
dict_1 = dict.fromkeys(seq)
print(dict_1)

dict_2 = dict.fromkeys(seq, 10)
print(dict_2)

# result
{'age': None, 'name': None, 'sex': None}
{'age': 10}
