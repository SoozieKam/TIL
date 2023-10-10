# BOJ 1748 수 이어 쓰기 1

N = int(input())

jari = len(str(N))

if jari == 1:
    print(N)
else:
    cnt = 9
    for i in range(2, jari):
        cnt += i * 9 * (10 ** (i-1))
    cnt += (N - 10 ** (jari-1) + 1) * jari
    print(cnt)