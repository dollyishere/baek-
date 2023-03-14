from pprint import pprint

# 보드 크기 N, 사과 개수 K 각각 입력 받음
N = int(input())
K = int(input())

# 게임 맵 임의로 생성해줌
game_map = [['X'] * N for _ in range(N)]
# 방향 적용되는 카운트와 방향 담아줄 direction_list 생성
direction_list = list()

# 동, 남, 서, 북
# 왼쪽으로 방향 전환 시 -1, 오른쪽으로 전환 시 +1 해주기 
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]] 

# 현재 뱀의 전체 위치 담아줄 snake 생성
snake = [[0, 0]]
# 현재 방향은 인덱스로 direction에서 뽑아올 것이므로, current_direct 변수 만든 후 초기값 0을 넣어줌
current_direct = 0
# 게임이 몇 초 동안 진행되는지 담아줄 game_cnt 생성
game_cnt = 0

# K 만큼 반복하며 사과가 위치한 좌표를 받아준 후, game_map의 해당 인덱스를 'A'를 넣어줌
for k in range(K):
    x, y = map(int, input().split())
    game_map[x - 1][y - 1] = 'A'

# 뱀이 지나간 자리를 구분하기 쉽게 STARTING 시점에 game_cnt를 넣어줌
# 앞으로도 뱀의 머리가 지나간 자리는 game_cnt로 대체할 것
game_map[0][0] = game_cnt

# 방향 수인 L을 받아줌
L = int(input())

# 예고된 방향 수만큼 for문 돌린 다음, 리스트화 시켜서 direction_list에 추가
for l in range(L):
    move_num, direct = input().split()
    direction_list.append([int(move_num), direct])

# 횟수가 명확히 정해지지 않았으므로, while문으로 반복함
while True:
    
    # 매 회차를 시작할 때마다, game_cnt를 1씩 더해줌
    game_cnt += 1
    
    # 현재 뱀의 머리 좌표와, 방향 좌표를 이용해 이번 회차의 뱀의 머리(snake_current_head를 구해줌)
    snake_current_head = [snake[0][0] + direction[current_direct][0], snake[0][1] + direction[current_direct][1]]

    # 만약 뱀의 머리가 맵을 벗어나거나, 자기 몸과 충돌한다면, 즉시 해당 회차를 종료함
    if snake_current_head[0] == -1 or snake_current_head[0] == N or snake_current_head[1] == -1 or snake_current_head[1] == N:
        break
    elif snake_current_head in snake:
        break

    # 만약 게임 종료 기준을 충족시키지 못했다면, 뱀의 몸을 다시 구성함
    # 현재 뱀의 머리를 change_snake라는 새 리스트 내에 넣은 후, 해당 리스트에 기존 뱀의 몸 좌표를 extend로 집어넣음
    # 이후 snake를 change_snake로 대체해줌
    change_snake = [snake_current_head]
    change_snake.extend(snake)
    snake = change_snake

    # 만약 뱀이 사과를 먹었다면, 길이가 늘어난 것이므로 꼬리를 삭제하지 않아도 됨
    # 하지만 먹지 못했다면 꼬리를 삭제해야 함
    # 만약 현재 뱀의 머리가 위치한 인덱스의 값이 'A'가 아니라면, pop을 이용해 꼬리를 없애줌
    if game_map[snake_current_head[0]][snake_current_head[1]] != 'A':
        snake_tail = snake.pop(-1)

    # 뱀 머리의 위치 확인을 위해 뱀 머리가 위치한 인덱스의 값을 game_cnt로 바꿔줌    
    game_map[snake_current_head[0]][snake_current_head[1]] = game_cnt

    # 만약 아직 방향 전환 지시가 있을 시, 이하 검증을 시도함
    # 먼저 현재 dirction_list에 가장 처음([0])에 위치한 지시가 현 시점에서 시도되어야 한다면,
    # 방향에 따라 -1 또는 +1한 후, 최소 최대값인 0이나 3을 벗어날 시 조정해줌
    if len(direction_list):
        change_direct = direction_list[0]
        if game_cnt == change_direct[0]:
            if change_direct[1] == 'L':
                current_direct -= 1
            else:
                current_direct += 1

            if current_direct > 3:
                current_direct = 0
            elif current_direct < 0:
                current_direct = 3

            # 이후, 해당 지시는 사라져야 하므로 pop으로 없애줌
            direction_list.pop(0)
    

# 정답 출력
print(game_cnt)