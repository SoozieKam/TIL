# BOJ 14889 스타트와 링크
# 브루트포스 알고리즘 (완전탐색)
# 백트래킹 

from itertools import combinations

N = int(input())
rank = []
result = []

for _ in range(N):
    rank.append(list(map(int, input().split())))

def divide(n, current=1, team1=[], team2=[]):
    sum_1 = 0
    sum_2 = 0
    temp = 1000000
    global result
    if current == n + 1:
        if len(team1) == n // 2 and len(team2) == n // 2:
            team1_combi= list(combinations(team1, 2))
            team2_combi = list(combinations(team2, 2))
            
            for c in team1_combi:
                sum_1 += rank[c[0]-1][c[1]-1] + rank[c[1]-1][c[0]-1]
            for c in team2_combi:
                sum_2 += rank[c[0]-1][c[1]-1] + rank[c[1]-1][c[0]-1]
             
            if abs(sum_1 - sum_2) == 0:
                result.append(0)
                return result 
            
            if abs(sum_1 -  sum_2) < temp:
                temp = abs(sum_1 - sum_2)
                result.append(temp)
            
        return result 
    
    if len(team1) < n // 2:
        divide(n, current + 1, team1 + [current], team2)
    
    if len(team2) < n // 2:
        divide(n, current + 1, team1, team2 + [current])

     
divide(N)
print(min(result))

