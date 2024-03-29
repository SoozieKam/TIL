# 제곱암호는 다음과 같은 특징을 가진다.
# 암호문의 길이를 N이라고 하면, N/2개의 숫자와 N/2개의 알파벳 소문자로 이루어져 있다. N은 항상 짝수이다. 숫자는 1~9 사이의 정수이다.
# 암호문의 첫 글자는 항상 알파벳 소문자이고, 이후에는 항상 숫자와 알파벳 소문자가 번갈아서 등장한다.

# 제곱암호로 암호화된 문장은 아래 방식을 통해 복호화할 수 있다.
# 원문은 처음에 비어있다.
# i가 홀수일 때, 암호문의 i번째 문자를 알파벳의 사전 기준 다음 문자로 바꾸는 작업을 암호의 i번째 숫자의 제곱번 시행한다.
# 작업이 끝난 뒤 변환된 알파벳을 원문의 맨 오른쪽에 추가한다. (i번째 숫자는 암호문의 i+1번째 문자에 해당한다.)
# z에서 사전 기준 다음 문자로 바뀌어야 하는 경우에는 a로 바뀌게 된다.
# 복호화가 끝난 뒤의 원문은 N/2 길이의 알파벳 소문자로만 이루어진 문자열이다.

# 제곱암호로 암호화된 문장을 원문으로 바꾸는 프로그램을 작성하시오.

# 예시 1
# 입력:
#    8
#    a1b2c3e4
# 출력:
#    bflu

# 예시 2
# 입력:
#     6
#     z2y2z1
# 출력:
#     dca

N = int(input())  # 암호문의 길이
S = input()
result = []

# print(chr(ord("b") + int("2") * int("2")))

for i in range(0, N - 1, 2):
    if ord(S[i]) + int(S[i + 1]) * int(S[i + 1]) >= 122:
        result.append(chr(ord(S[i]) + int(S[i + 1]) * int(S[i + 1]) - 26))
    else:
        result.append(chr(ord(S[i]) + int(S[i + 1]) * int(S[i + 1])))

print("".join(result))
