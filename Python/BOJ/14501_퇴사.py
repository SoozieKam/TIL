# BOJ 14501 퇴사

# dp (동적계획법) 사용

N = int(input())

t = []
p = []
dp = [0] * (N + 1)

for _ in range(N):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

for i in range(N - 1, -1, -1):
    print(dp)
    # i일에 상담하면 퇴사일자 넘는 경우
    if i + t[i] > N:
        dp[i] = dp[i + 1]
        print(dp)
    else:
        # i일에 상담을 하는 경우와 하지 않는 경우 중 비용이 큰 값으로 선택
        dp[i] = max(dp[i + t[i]] + p[i], dp[i + 1])
        print(dp)

print(dp[0])
