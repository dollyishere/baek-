import sys

# 현재까지 사용한 운동기구 리스트, 현재 몸무게 동시에 넘겨줌
def dfs(use_list, now_weight):
    # 전역 변수 answer 선언함
    global answer

    # 만약 use_list의 길이가 N과 같다면, 모든 운동기구가 사용된 것임
    # 함수 실행 조건 자체가 now_weight가 500 이상일 때이므로, answer에 1씩 더해줌
    if len(use_list) == N:
        # print(use_list, now_weight)
        if now_weight >= 500:
            answer += 1
    # 만약 모든 운동기구가 사용되지 않았을 시, 매일의 운동 루틴을 시작함
    else:
        # N 만큼의 운동기구가 있으므로, for문으로 순회
        for a_kit in range(N):
            # 만약 use_list에 a_kit가 없다면, 해당 번호의 운동기구는 사용되지 않았다는 뜻임
            # 따라셔 use_list에 a_kit(운동기구 번호=인덱스)를 넣어주고, now_weight에 해당 운동 기구로 얻을 수 있는 근량을 더해줌
            # 여기서 인덱스 번호로 운동기구를 구분한 이유는 같은 중량인 운동기구가 있을 가능성을 염두했기 때문임
            if a_kit not in use_list:
                use_list.append(a_kit)
                now_weight += (a_kit_list[a_kit] - K)
                # 만약 now_weight 값이 500 이상이라면, dfs 그 시점에서 재시작함
                if now_weight >= 500:
                    dfs(use_list, now_weight)
                # 다양한 가능성을 점치기 위해, now_weight와 use_list에서 더했거나 집어넣었던 값 빼줌
                now_weight -= (a_kit_list[a_kit] - K)
                use_list.pop(-1)

# 일수 N, 근손실량 K 입력받음
N, K = map(int, sys.stdin.readline().split())
# 운동 기구가 담긴 a_kit_list 입력받음
a_kit_list = list(map(int, sys.stdin.readline().split()))

# 현재 몸무게를 weight에 배정
weight = 500
# 정답 계산해 담아줄 answer를 초기값 0으로 지정해줌
answer = 0
# 함수 실행함
dfs([], weight)
# 이후 정답 출력함
print(answer)