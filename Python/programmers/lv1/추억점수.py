# 사진들을 보며 추억에 젖어 있던 루는 사진별로 추억 점수를 매길려고 합니다. 사진 속에 나오는 인물의 그리움 점수를 모두 합산한 값이 해당 사진의 추억 점수가 됩니다. 예를 들어 사진 속 인물의 이름이 ["may", "kein", "kain"]이고 각 인물의 그리움 점수가 [5점, 10점, 1점]일 때 해당 사진의 추억 점수는 16(5 + 10 + 1)점이 됩니다. 다른 사진 속 인물의 이름이 ["kali", "mari", "don", "tony"]이고 ["kali", "mari", "don"]의 그리움 점수가 각각 [11점, 1점, 55점]]이고, "tony"는 그리움 점수가 없을 때, 이 사진의 추억 점수는 3명의 그리움 점수를 합한 67(11 + 1 + 55)점입니다.

# 그리워하는 사람의 이름을 담은 문자열 배열 name, 각 사람별 그리움 점수를 담은 정수 배열 yearning, 각 사진에 찍힌 인물의 이름을 담은 이차원 문자열 배열 photo가 매개변수로 주어질 때, 사진들의 추억 점수를 photo에 주어진 순서대로 배열에 담아 return하는 solution 함수를 완성해주세요.


# 풀이
def solution(name, yearning, photo):
    memory = dict(zip(name, yearning))
    cnt = 0
    cnt_list = []
    for i in range(len(photo)):
        for j in photo[i]:
            if j in memory.keys():
                cnt += memory[j]
        cnt_list.append(cnt)
        cnt = 0
    return cnt_list

# 새로 배운 점 
# 1) zip이라는 새로운 함수를 알게 되었다. 
# zip이란? 두 개의 배열을 하나의 쌍으로 묶어 주는 함수이다. 
# 예) 

# numbers = [1, 2, 3]
#     letters = ["A", "B", "C"]
#     for pair in zip(numbers, letters):
# ...     print(pair)
# ...
# (1, 'A')
# (2, 'B')
# (3, 'C')

# 2) enumerate() 함수는 내용과 인덱스를 튜플로 묶어 주는 함수이다. 
# 예)
# for entry in enumerate(['A', 'B', 'C']):
# ...print(entry)
# ...
# (0, 'A')
# (1, 'B')
# (2, 'C')
