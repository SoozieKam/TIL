# 프로그래머스 '옹알이(1)'

""" 조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음을 최대 한 번씩 사용해 조합한(이어 붙인) 발음밖에 하지 못합니다. 문자열 배열 babbling이 매개변수로 주어질 때, 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.

 
# 테스트 케이스 
babbling = ["aya", "yee", "u", "maa", "wyeoo"]	
return 값 = 1 """


def solution(babbling):
    result = 0
    baby = ['aya', 'ye', 'woo', 'ma']
    for i in range(len(babbling)):
        for j in baby:
            if j in babbling[i]:
                babbling[i] = babbling[i].replace(j, ' ')

    for i in babbling:
        if len(i.strip()) == 0:
            result += 1

    return result


""" 처음에는 ''로 replace했었는데, 테스트케이스의 마지막 인덱스 요소 'wyeoo'처럼 replace했을 때 그 앞의 문자와 뒤의 문자가 이어지면서 baby 리스트 안의 값이 새로 만들어질 수도 있다!
'' 대신 ' '로 replace한 후 strip으로 빈칸 삭제해주면 된다."""

# strip이 생각이 안나서 아래와 같이 비효율적인 방법으로 코드를 짰었다.
# if i == ' ' or i == '  ' or i == '   ' or i == '    ' :
