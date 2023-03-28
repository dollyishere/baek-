import sys
from collections import deque

# 트럭 개수 n, 다리 길이 w, 다리 최대 하중 L 입력 받음
n, w, L = map(int, sys.stdin.readline().split())
# 트럭의 무게를 입력받아 trucks_weight에 집어넣어줌
trucks_weight = list(map(int, sys.stdin.readline().split()))

# 정답으로 입력할 총 시간 time_cnt, 현재까지 지나간 트럭의 수를 셀 trucks_cnt를 각각 생성
time_cnt = 0
trucks_cnt = 0

# 현재 다리 위에 올라가 있는 트럭의 상황을 담아줄 bridge_state, 다리 위 트럭의 총 무게를 담아줄 bridge_weigth 각각 생성
bridge_state = deque([])
bridge_weight = 0

# 총 몇 단위시간동안 반복될 지 알 수 없으므로, while문으로 탈출할 때까지 이하 로직 반복
while True:
    # 매 단위 시간이 시작될 때마다, time_cnt를 1씩 늘려줌
    time_cnt += 1

    # 만약 현재 다리 위에 트럭이 하나 이상 올라가 있다면(=bridge_state 안에 하나라고 인자가 있다면) 트럭을 이동시킴
    if len(bridge_state):
        # 변화된 다리 상황을 담아줄 new_state 생성
        new_state = deque([])
        # bridge_state가 빌 때까지 반복함
        while bridge_state:
            # 먼저 bridge_state 맨 앞의 요소를 popleft를 통해 빼서 now_truck 변수에 담아줌
            # 후술하겠지만, 여기서 now_truck은 [해당 트럭의 무게, 현재 위치에서 다리 끝까지 얼마나 남았는지(초기 값 w)]를 인자 값으로 가지고 있는 리스트임
            now_truck = bridge_state.popleft()
            # 그리고 now_truck의 1번 인덱스에 있는 값(위치값)을 -1 해줌
            now_truck[1] -= 1
            # 만약 이동하고도 아직 해당 트럭이 다리에 도착하지 못했다면(즉, 1번 인덱스 값이 1 이상이라면), 아직 다리를 벗어나지 못한 트럭임
            # 따라서 변경된 값 그대로 new_state에 추가해줌
            if now_truck[1]:
                new_state.append(now_truck)
            # 만약 다리 위에 없다면, 해당 트럭의 무게를 bridge_weight에서 빼줌
            else:
                bridge_weight -= now_truck[0]
        # 모든 트럭의 이동이 끝났다면, bridge_state를 new_state로 교체해줌
        bridge_state = new_state

    # 만약 아직 트럭이 전부 다리 위를 지나가거나 지나가는 중이 아니라면, truck_cnt는 n보다 작은 값일 것임
    # 따라서 경우에 따라 남은 트럭을 이동시켜야 함
    if trucks_cnt < n:
        
        # 만약 현재 다리 위에 올라가 있는 트럭의 무게 총합과 대기 중인 트럭의 값의 합이 L(다리 최대하중)보다 작거나 같다면
        # bridge_state에 해당 트럭의 무게 값과 앞으로 이동해야 할 거리 w 값을 인자로 가진 리스트를 추가해줌
        # 그리고 brige_weight에 해당 트럭의 무게를 추가해준 후, trucks_cnt를 +1 해줌
        if bridge_weight + trucks_weight[trucks_cnt] <= L:
            bridge_state.append([trucks_weight[trucks_cnt], w])
            bridge_weight += trucks_weight[trucks_cnt]
            trucks_cnt += 1

    # 만약 모든 트럭이 다리를 완전히 지나간 상태라면, 모든 이동이 완료된 것이므로 break로 빠져나옴
    if trucks_cnt == n and len(bridge_state) == 0:
        break
    
# 정답 출력해줌
print(time_cnt)