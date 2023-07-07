# 첫째 줄에 땅의 길이 N과 폭탄의 개수 K가 공백을 기준으로 주어진다.
# 다음 k개 줄에는 폭탄을 떨어트릴 좌표의 값 y1, x1이 공백을 두고 주어진다.
# 폭탄을 모두 떨어트렸을 때, N*N 안의 모든 땅의 폭탄 값의 합을 출력한다.

# 예시 1
# 3 3
# 3 3
# 3 3
# 1 1
# 출력 : 9

# 예시 2
# 4 4
# 1 1
# 4 4
# 3 3
# 2 4
# 출력 : 15

N, K = map(int, input().split())
sum = 0
for _ in range(K):
    y, x = map(int, input().split())
    if 1 < y < N and 1 < x < N:
        sum += 5
    elif y in [1, N] and x in [1, N]:
        sum += 3
    elif y in [1, N] and 1 < x < N:
        sum += 4
    else:
        sum += 4

print(sum)
