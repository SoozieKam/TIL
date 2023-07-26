# 한 변의 길이가 N인 정사각형 모양의 땅에 개미와 진딧물이 있다.
# 개미는 거리 M 이하에 위치한 진딧물에게서 수액을 체취할 수 있다.
# 이 수액이 없다면 굶주린 개미는 다른 곳으로 먹이를 찾아 떠나게 된다. 이때 거리는 맨해튼 거리이다.
# 현재 땅에 있는 개미와 진딧물의 위치가 주어졌을 때, 진딧물로부터 수액을 얻을 수 있는 개미의 수를 구해 보자.
# 주어지는 숫자는 0, 1, 2 중 하나이다. 0은 빈 위치, 1은 개미가 있는 위치, 2는 진딧물이 있는 위치임을 의미한다.

# 힌트
# 두 지점 사이의 맨해튼 거리는 한 지점의 좌표가 (a, b)이고 다른 지점의 좌표가 (c, d)일 때 두 지점 사이의 거리는 |a-c| + |b-d| 이다.

# 예시 1
# 입력 :
#       4 2
#       2 0 0 0
#       2 0 0 1
#       2 0 0 0
#       2 0 0 1
# 출력 :
#       0

# 예시 2
# 입력 :
#       4 2
#       0 1 0 0
#       0 2 0 1
#       0 0 0 1
#       2 0 1 0
# 출력 :
#       3

N, M = map(int, input().split())
# world = [[] for _ in range(N)]
world = []

for i in range(N):
    a = list(map(int, input().split()))
    world.append(a)

# print(world)

ant = []
food = []

for i in range(len(world)):
    for j in range(len(world[i])):
        if world[i][j] == 1:
            ant.append((i, j))
        if world[i][j] == 2:
            food.append((i, j))

print(ant)
print(food)

result = 0

for a in ant:
    for f in food:
        if abs(a[0] - f[0]) + abs(a[1] - f[1]) <= M:
            result += 1

print(result)


# 0 0 0 0 0 0
# 0 0 2 0 0 0
# 0 2 2 2 0 0
# 2 2 0 2 2 0
# 0 2 2 2 0 0
# 0 0 2 0 0 0
