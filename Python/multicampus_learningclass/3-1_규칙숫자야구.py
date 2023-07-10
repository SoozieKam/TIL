# 3-1 규칙 숫자 야구

# 4자리 규칙 숫자 야구, 처음 입력을 기반으로 정답을 찾아감
# Strike 는 입력의 i번째 값이 정답에 포함, 위치도 같은 경우
# Ball 은 입력의 i번째 값이 정답에 포함, 위치는 같지 않은 경우
# Fail 은 입력의 i번째 값이 정답에 포함 X
# Strike 4개가 되면 게임에서 승리

# 아래와 같은 순서로 진행
# 1. 정답과 입력을 비교해서 현재 자리의 값이 strike, ball, fail 중 어떤 상태에 해당되는지 판단한다.
# 정답과 입력이 일치하면 게임에서 승리, break.
# 2. 가장 왼쪽 자리부터 순서대로 아래 과정 반복.
# 1. 현재 자리 값이 strike면 아무것도 안함
# 2. 현재 자리 값이 fail 이면 현재 자리 값에 1 더하고 10으로 나눔. 만약 계산한 값이 다른 자리에 존재하면, 존재하지 않을 때까지 반복
# 3. 2번 과정에서 ball 인 자리가 있다면, 판단 결과 중에서 strike 자리를 제외한 나머지 자리를 모두 오른쪽으로 한 칸씩 옮긴다.
# 옮길 자리가 없으면 strike가 아닌 가장 왼쪽 자리로 이동한다.

# 구름이가 규칙에 따라 게임을 진행했을 때, 승리하기 위해 위 과정을 몇 번 수행해야 하는지 구하시오.

# 인풋 예시
# 0123
# 1234
# 답 : 4

answer = list(map(int, input()))
user_input = list(map(int, input()))

# strike, ball, fail을 판단하는 로직

# 0. 우선 과정을 수행한 횟수를 나타내는 변수를 만든다.
make_input_count = 0

# 1. 정답과 사용자 인풋값을 비교해서 0 = strike, 1 = ball, 2 = fail 로 정한다.
# 2. result의 모든 상태는 기본적으로 fail로 둔다.
while True:
    make_input_count += 1
    result = [2, 2, 2, 2]

    # user_input과 answer이 같은 경우 게임이 종료된다.
    if user_input == answer:
        print(make_input_count)
        break

    # 3. 입력의 첫째 자리부터 순서대로 보면서 현재 값이 정답에 포함되는지 판단한다. 포함된다면 3으로 넘어가고, 아니라면 다음 자리로 넘어간다.
    for i in range(4):
        # 현재 값이 answer에 없는 경우 fail, 근데 기본값을 fail로 설정했으니 그냥 넘어가면 된다.

        # 4. 현재 값과 입력값이 자리까지 동일하다면 strike, 아니면 ball로 상태를 확정한다.
        # 아래는 strike인 경우
        if user_input[i] in answer:
            if user_input[i] == answer[i]:
                result[i] = 0

            # ball인 경우
            else:
                result[i] = 1

# fail인 경우 처리하는 로직
# 반복적으로 일어나는 과정이므로, 따로 함수를 만들면 가독성이 높아진다!

# fail() 함수는 fail 상태에 해당하는 자리를 문제의 요구사항에 따라 변경하는 함수. 아래 조건을 만족하도록 구현해야 한다.

# - 인풋값의 첫 번째 자리부터 순서대로 작업을 수행한다.
# - fail 상태에 해당하는 자리만 작업을 수행한다.
# - 현재 값을 1 증가시킨 뒤 10으로 나눠준다.
# - 증가시킨 값이 인풋값의 다른 값과 겹치지 않을 때까지 반복한다.


def fail():
    for i in range(4):
        if result[i] != 2:
            continue

        # 조건을 만족하는 값이 나올 때까지 아래 과정을 반복한다.
        while True:
            # 현재 자리의 값을 1 증가
            # 값을 바로 대입하지 않고, 현재 인풋값의 다른 자리에 해당 값이 존재하는지를 먼저 판단한다.

            temp = (user_input[i] + 1) % 10
            out = temp not in user_input
            user_input[i] = temp
            if out:
                break


# ball 인 경우 처리하는 로직
# ball() 함수를 만들어서 인풋값을 오른쪽으로 한칸씩 옮겨 주는 역할을 하도록 한다.
# deque 자료구조 활용하면 효율적이긴 함. (근데 여기선 네 자리밖에 안돼서 그냥 리스트로 풀기)
# strike가 아닌 위치를 pos, 그 위치의 값을 저장하는 리스트를 value 라고 명명한다.


def ball():
    if 1 not in result:
        return
    pos = []
    value = []

    for i in range(4):
        if result[i] != 0:
            pos.append(i)
            value.append(user_input[i])

    for i in range(len(pos)):
        if i == 0:
            user_input[pos[i]] = value[-1]
        else:
            user_input[pos[i]] = value[i - 1]


fail()
ball()
