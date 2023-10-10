# BOJ 3085 사탕 게임

N = int(input())
candy = [[] for _ in range(N)]

for i in range(len(candy)):
    candy[i].extend(input())

cnt = []
int_cnt = 1
int_cnt_2 = 1
temp = 1
temp_2 = 1
target = [0]

# 연속되는 사탕이 제일 많은 행 찾기
for i in range(N):
    for j in range(N - 1):
        if candy[i][j] == candy[i][j + 1]:
            temp += 1
        else:
            if temp >= 2:
                if i >= 1:
                    if candy[i - 1][j] == candy[i][j - 1]:
                        if int_cnt < temp:
                            int_cnt = temp
                            if j > 0:
                                target[0] = (i, j)
                            else:
                                target[0] = (i - 1, N - 1)
                elif i <= N - 2:
                    if candy[i + 1][j] == candy[i][j - 1]:
                        if int_cnt < temp:
                            int_cnt = temp
                            if j > 0:
                                target[0] = (i, j)
                            else:
                                target[0] = (i - 1, N - 1)

            temp = 1
print(target)
print(int_cnt)

# 연속되는 사탕이 제일 많은 열 찾기
for j in range(N):
    for i in range(N - 1):
        if candy[i][j] == candy[i + 1][j]:
            temp_2 += 1
        else:
            if temp >= 2:
                if j >= 1:
                    if candy[i][j - 1] == candy[i - 1][j]:
                        if int_cnt < temp_2:
                            int_cnt = temp_2
                            if i > 0:
                                target[0] = (i, j)
                            else:
                                target[0] = (N - 1, j)
                elif j <= N - 2:
                    if candy[i][j + 1] == candy[i - 1][j]:
                        if int_cnt < temp_2:
                            int_cnt = temp_2
                            if i > 0:
                                target[0] = (i, j)
                            else:
                                target[0] = (N - 1, j)

            temp = 1


print(target)
print(int_cnt)

print(int_cnt + 1)

# [행+1][열]의 사탕 종류가 b이면 print(N)
# [행-1][열]의 사탕 종류가 b이면 print(N)
# 둘 다 아니면 print(N-1)
