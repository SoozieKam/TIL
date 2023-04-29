# 공원산책
# 지나다니는 길을 'O', 장애물을 'X'로 나타낸 직사각형 격자 모양의 공원에서 로봇 강아지가 산책을 하려합니다. 산책은 로봇 강아지에 미리 입력된 명령에 따라 진행하며, 명령은 다음과 같은 형식으로 주어집니다.

# ["방향 거리", "방향 거리" … ]
# 예를 들어 "E 5"는 로봇 강아지가 현재 위치에서 동쪽으로 5칸 이동했다는 의미입니다. 로봇 강아지는 명령을 수행하기 전에 다음 두 가지를 먼저 확인합니다.

# 주어진 방향으로 이동할 때 공원을 벗어나는지 확인합니다.
# 주어진 방향으로 이동 중 장애물을 만나는지 확인합니다.
# 위 두 가지중 어느 하나라도 해당된다면, 로봇 강아지는 해당 명령을 무시하고 다음 명령을 수행합니다. 

# 공원을 나타내는 문자열 배열 park, 로봇 강아지가 수행할 명령이 담긴 문자열 배열 routes가 매개변수로 주어질 때, 로봇 강아지가 모든 명령을 수행 후 놓인 위치를 [세로 방향 좌표, 가로 방향 좌표] 순으로 배열에 담아 return 하도록 solution 함수를 완성해주세요.


# 풀이 
def solution(park, routes):
    way =  {'E':(0,1), 'W':(0,-1), 'S':(1,0), 'N':(-1,0)}
    obs_list = []
    cnt = 0
    
    # 시작점 설정
    for x in range(len(park)):
        if 'S' in park[x]:
            y = park[x].index('S')
            start = (x, y)
            break
    
    # 장애물 설정 
    for x in range(len(park)):
        for y in range(len(park[x])):
            if park[x][y] == 'X':
                obs = (x, y)
                obs_list.append(obs)
          
    # print(start)
    # print(obs_list)
    
    for i in range(len(routes)):
        # 동쪽 혹은 서쪽으로 이동할 때 
        if routes[i][0] == 'E' or routes[i][0] == 'W':
            x_1 = start[0]
            y_1 = start[1] + way[routes[i][0]][1] * int(routes[i][2])
            
            # park 범위 벗어나지 않는지 확인
            if 0 <= x_1 < len(park) and 0 <= y_1 < len(park[0]):
                
                # 동쪽으로 이동 시
                if y_1 > start[1]:
                    # 이동 방향에 장애물 있는지 체크 
                    for j in range(start[1], y_1 + 1):
                        if (x_1, j) not in obs_list: 
                            cnt += 1
                            # print(cnt)
                            
                    # 이동 방향에 장애물이 없으면
                    if cnt == y_1 +1 - start[1]:
                        start = (x_1, y_1)
                
                # 서쪽으로 이동 시       
                else:
                    for j in range(y_1, start[1] + 1):
                        if (x_1, j) not in obs_list: 
                            cnt += 1
                            # print(cnt)
                            
                    # 이동 방향에 장애물이 없으면 
                    if cnt == start[1] + 1 - y_1:
                        start = (x_1, y_1)
                        
                cnt = 0
                # print(start)
        
        # 남쪽 혹은 북쪽으로 이동할 때
        else: 
            
            x_2 = start[0] + way[routes[i][0]][0] * int(routes[i][2])
            y_2 = start[1]
            
            # park 범위 벗어나지 않는지 확인
            if 0 <= x_2 < len(park)  and 0 <= y_2 < len(park[0]):
                
                # 남쪽으로 이동 시
                if x_2 > start[0]:  
                    # 이동 방향에 장애물 있는지 체크
                    for j in range(start[0], x_2 + 1):
                        if (j, y_2) not in obs_list: 
                            cnt += 1
                            # print(cnt)
                    
                    # 이동 방향에 장애물이 없으면         
                    if cnt == x_2 +1 - start[0]:
                        start = (x_2, y_2)
                        
                # 북쪽으로 이동 시
                else:
                    # 이동 방향에 장애물 있는지 체크
                    for j in range(x_2, start[0] + 1):
                        if (j, y_2) not in obs_list: 
                            cnt += 1
                            # print(cnt)
                            
                    # 이동 방향에 장애물이 없으면         
                    if cnt == start[0] + 1 - x_2:
                        start = (x_2, y_2)   
                    
                cnt = 0
                # print(start)
                         
    return list(start)     
    
    # 문제1) 처음에는 아래와 같이 썼는데, typeerror가 났다. list와 tuple의 값이 같은지 비교해서 생긴 오류.  
    # for j in obs_list:
        # if x_2 != obs_list[j][0] and y_2 != obs_list[j][1]:  
    # 해결1) 리스트를 없애고 튜플로 통일
    
    # 문제2) 원래 park 리스트 안의 장애물 값을 찾기 위해 .index() 메서드를 사용했는데, 그러면 값을 다 찾을 수 없다. 몇 개인지도 모르니까.  
    # 해결2) for문을 두 번 돌려서 x, y 값을 다 찾았다.
    
    # 문제3) 이렇게 하면 목적지로 가는 길에 있는 장애물을 못 발견한다 ...
    # if (x_2, y_2) not in obs_list: 
    #    start = (x_2, y_2)
    # 해결3) for문으로 반복을 돌려서 장애물을 하나씩 찾아야 한다. 
    
    # 문제4) 테스트케이스는 통과가 다 되는데 문제가 통과되지 않아서 새로 테스트케이스를 만들어 보니, 
    # 서쪽이나 북쪽으로 가는 길에 장애물이 있을 때는 통과가 되지 않았다. 이동 방향에 장애물이 있는지 체크할 때 -로 이동하는 경우가 있다는 걸 생각하지 못했다.
    # 해결4) 동서남북을 다 분리해서 for문을 돌림. 
    
    # 주의! cnt값 0으로 만들어 주는 거 잊지 말자. 
    # cnt = 0 이 어느 범위에 있는지 잘 체크. 
    
