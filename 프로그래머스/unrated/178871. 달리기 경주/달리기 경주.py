def solution(players, callings):
    answer = []
    now_race = {}
    now_race_rev = {}
    
    for i in range(0, len(players)):
        now_race[i] = players[i]
        now_race_rev[players[i]] = i

    for calling in callings:
        # 현재 추월한 사람 현 등수 먼저 구하기
        now_here = now_race_rev[calling]
        # 추월 당한 사람 구하기
        out_there = now_race[now_here-1]

        # 등수 변경
        now_race[now_here-1] = calling
        now_race_rev[calling] = now_here-1
        
        now_race[now_here] = out_there
        now_race_rev[out_there] = now_here
    
    for racer in now_race:
        answer.append(now_race[racer])
    
#     # 불린 수가 많을수록 추월을 많이 했다는 뜻
#     # 먼저 최대 포인트를 정한 후, 등수가 높은 순으로 player_point의 해당하는 인덱스에 높은 점수를 배정
#     point = len(players)
#     player_point = []
#     for now_player in range(0, len(players)):
#         player_point.append(point)
#         point -= 1
    
#     # callings 순회
#     # 이 문제의 핵심은, 추월에 있음
#     # 추월한 플레이어가 점수를 1점 더 가져가는 대신, 본래 해당 순위였던 플레이어는 점수를 1점 잃게 됨
#     # 두 사람의 점수가 동등하다면 index로 정확한 값을 끌어낼 수 없으므로, 먼저 추월당한 플레이어의 점수를 깎은 후 추월한 플레이어의 점수를 높임
#     for now_player in callings:
#         now_player_state = players.index(now_player)
#         player_point[player_point.index(player_point[now_player_state] + 1)] -= 1
#         player_point[now_player_state] += 1
    

#     # 이후 최종 점수 검증
#     # 현재 player_point에서 최대 득점인 플레이어를 index로 찾아냄
#     # 이후 answer에 해당 플레이어의 이름을 넣은 후, 해당 플레이어의 점수는 0으로 초기화 하는 것으로 차후 점수 검증에서 배제함
#     for _ in range(len(players)):
#         now_top = player_point.index(max(player_point))
#         answer.append(players[now_top])
#         player_point[now_top] = 0        
    
    # 시간초과
    # for now_player in callings:
    #     now_player_state = players.index(now_player)
    #     first_player = players[now_player_state - 1]
    #     answer[now_player_state - 1] = now_player
    #     answer[now_player_state] = first_player
    #     answer = players
    
    # 답 리턴
    return answer