from pprint import pprint
def solution(maps):
    # 1. 레버부터 찾는다
    # 2. 그 뒤에 출구를 찾는다
    # 따라서 bfs는 총 2번 이루어져야 함

    answer = 0
    # 델타탐색용 리스트 moving과 현재 맵 세로 가로 길이(x, y) 찾아서 변수화해줌
    moving = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    x, y = len(maps), len(maps[0])
    
    # 어디서부터 시작해야 하는지 해당 인덱스 값을 2중 반복문으로 찾아낸 후, start_here에 넣어줌
    # 이후 시간 절약을 위해 break로 탈출함
    start_here = []
    for i in range(x):
        for j in range(y):
            if maps[i][j] == "S":
                start_here = [i, j]
                break

    # bfs 2번 사용하니 함수화
    # 어디에서 시작해야 하는지(start_here, int), 어디로 가고 싶은지(want_go, string)를 인자로 받음
    def bfs(start_here, want_go):
        queue = [[start_here, 0]]
        visited = [[True] * y for _ in range(x)]
        end_here = []
        time_check = 1
        while queue and end_here == []:
            now_here = queue.pop(0)
            for k in range(4):
                di = now_here[0][0] + moving[k][0]
                dj = now_here[0][1] + moving[k][1]
                if 0 <= di < x and 0 <= dj < y and visited[di][dj] and maps[di][dj] != "X":
                    if maps[di][dj] == want_go:
                        pprint(visited)
                        end_here = [di, dj]
                        time_check = now_here[1] + 1
                        break
                    else:
                        visited[di][dj] = False
                        queue.append([[di, dj], now_here[1]+1])
        
        # 현재 bfs를 돌려본 결과, 어디서 끝마쳤는지, 시간은 얼마나 걸렸는지를 리턴함
        # 이때 만약 정상적으로 길을 찾지 못했다면, end_here은 여전히 빈 리스트일 것임
        return end_here, time_check
    
    # laber_find에 레버를 bfs로 찾은 결과를 받아줌
    laber_find = bfs(start_here, "L")
    # 만약 첫 인덱스가 비어있다면, 찾는데에 실패한 것이므로 answer 값을 -1로 설정해주고, 출구는 찾지 않음(시간 절약)
    if laber_find[0] == []:
        answer = -1
    # 만약 비어있지 않다면, 성공적으로 레버를 당긴 것임
    # 따라서 걸린 시간 값을 answer에 더해준 후, 이번에는 출구를 bfs를 통해 찾아줌
    # 이하의 로직은 이전과 같음
    else:
        answer += laber_find[1]
        exit_find = bfs(laber_find[0], "E")
        if exit_find[0] == []:
            answer = -1
        else:
            answer += exit_find[1]
    
    # 정답 리턴
    return answer