def solution(park, routes):
    answer = []
    # 로봇 강아지 이동 방향 딕셔너리로 뽑아낼 수 있도록 조정
    moving = {"E": [0, 1], "W": [0, -1], "S": [1, 0], "N": [-1, 0]}
    # park 세로 가로 길이 x, y에 담아줌
    x, y = len(park), len(park[0])
    # 시작 전 로봇강아지 초기 위치 설정
    for i in range(x):
        for j in range(y):
            if park[i][j] == "S":
                answer = [i, j]
                break
    
    # 명령 실행
    for route in routes:
        # 현재 이동 방향(now_moving), 만약 지시대로 이동했을 시 각 이동 턴마다의 위치(now_here), 실제로 수행 가능한 지시인지 판별할 flag 변수 생성
        now_moving = moving[route[0]]
        flag = True
        now_here = [answer[0], answer[1]]

        # 이동하는 칸의 수(int(route[2]))만큼 반복, 이동 방향에 맞는 값을 now_here의 각 인덱스에 더해줌      
        for now_turn in range(int(route[2])):
            now_here[0] += now_moving[0]
            now_here[1] += now_moving[1]
            # 만약 범위 내에 있고, 장애물 없을 시에는 pass, 아닐 시에는 flag 값을 False로 바꿔주고 탈출함(추가 검증 불필요)
            if 0 <= now_here[0] < x and 0 <= now_here[1] < y and park[now_here[0]][now_here[1]] != "X":
                pass
            else:
                flag = False
                break
        # 만약 flag가 True일 시, 지시 이행 가능함
        # 따라서 answer의 값을 실제 지시대로 이동했을 시의 도착 지점(now_here)로 교체함
        if flag:
            answer = now_here

    # 연산 끝난 후 답 리턴
    return answer