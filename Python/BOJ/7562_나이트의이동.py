# BOJ 7562 나이트의 이동 
# 그래프 
# 너비우선탐색 
from collections import deque 

T = int(input())

for _ in range(T):
    L = int(input())
    chess = [[0] * L for _ in range(L)]
    current_i, current_j = map(int, input().split())
    want_i, want_j = map(int, input().split())
    
    chess[current_i][current_j] = 1
    
    dx = [-1, 1, -2, 2, -2, 2, -1, 1]
    dy = [-2, -2, -1, -1, 1, 1, 2, 2]
    
    result = 0  
    
    queue = deque()
    queue.append((current_i, current_j, 0))
    
    while queue:
        temp = queue.popleft()
        
        if temp[0] == want_i and temp[1] == want_j:
            print(temp[2])
            break
        
        for i in range(8):
            next_i = dx[i] + temp[0]
            next_j = dy[i] + temp[1]
            
            if 0 <= next_i < L and 0 <= next_j < L and chess[next_i][next_j] == 0:
                chess[next_i][next_j] = 1
                queue.append((next_i, next_j, temp[2]+1))
                
            
    
#    while current_i != want_i or current_j != want_j:  
#        for i in range(8):
#            next_i = current_i + dx[i]
#            next_j = current_j + dy[i]
#            
#            if 0 <= next_i < L and 0 <= next_j < L:
#                if next_i == want_i and next_j == want_j:
#                    result += 1
#                    print(result)
#                    break  
#                else:
#                    current_i = next_i
#                    current_j = next_j
#                    result += 1
#                    print(result)
#    print(result)
    
 
# 바보같은 실수 ... i와 result값이 루프 돌때마다 초기화되게 함 ㅎ 
    
#    while True:
        # i = 0
        # result = 1

        # if 0 <= current_i + dx[i] <= l and 0 <= current_j + dy[i] <= l:
        #     if want_i== current_i + dx[i] and want_j == current_j + dy[i] :
        #         print(result)
        #         break
        #     else:
        #         current_i = current_i + dx[i]
        #         current_j = current_j + dy[i]
        #         result += 1 
        #         i += 1
            