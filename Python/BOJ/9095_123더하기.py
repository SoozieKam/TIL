# BOJ 9095 1,2,3 더하기
# dp

T = int(input())

def func(num):
    dp = [0] * (max(4, num+1))
    dp[1], dp[2], dp[3] = 1, 2, 4
    print(dp)
    for i in range(4, num+1, 1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        print(dp)
    return dp[num]

for _ in range(T):
    print(func(int(input())))