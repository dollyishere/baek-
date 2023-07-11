import math

# 플로이드-워셜로 풀이
# 유저 수, 친구 관계 수 n, m 각각 입력받음
# 이후 친구 관계 담아줄 friend_state를 생성, 각 인덱스에 inf 값을 담아줌
n, m = map(int, input().split())
friend_state = [[math.inf] * n for _ in range(n)]

# m만큼 반복함
# 친구 관계를 입력 받아준 후, friend_state에 각각 쌍방 친구 관계를 기록함(1)
for _ in range(m):
    now_people, their_friend = map(int, input().split())
    friend_state[now_people-1][their_friend-1] = 1
    friend_state[their_friend-1][now_people-1] = 1
    
# 플로이드-워셜 수행
# 만약 k를 경우해가는 것이 i와 j가 직접 연결되는 값보다 작다면, 해당 값으로 교체해줌
for k in range(n):
    for i in range(n):
        for j in range(n):
            if friend_state[i][j] > friend_state[i][k] + friend_state[k][j]:
                friend_state[i][j] = friend_state[i][k] + friend_state[k][j]

# 케빈 베이컨의 수가 가장 작은 사람이 누구인지 담아줄 answer과, 케빈 베이컨 수 최소값을 담아줄 min_bacon 생성
# min_bacon의 경우 정확성을 위해 inf 값을 배정
answer = 0
min_bacon = math.inf

# for문으로 n만큼 반복
# 만약 해당 인물의 케빈 베이컨 값이 현재까지 알아낸 최소 케빈 베이컨 수보다 작다면,
# 위 두 가지 수치를 해당 인물의 수치로 바꿔줌
for i in range(n):
    if sum(friend_state[i]) < min_bacon:
        answer = i
        min_bacon = sum(friend_state[i])

# 정답 출력
# 이때 정확도를 위해 인덱스 값이 1씩 줄어 있으므로, 1을 더해야 정확한 값이 나옴
print(answer+1)