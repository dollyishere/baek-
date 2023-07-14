import sys
# 윈도우 슬라이딩 기법으로 메모리 찰 것 같으면 바로 버리게 해야 하는 듯?
# 따라서 판정할 데이터만 남겨두고 매번 리셋할 것
# 첫 줄의 경우 판정할 필요 없으니 입력받은 후 바로 배정
# 최대 최소값은 따로 구해야 하므로(dp의 경우 한 리스트 당 한 갈래로밖에 판정 불가) 리스트 따로 만들어주기
n = int(input())

first_line = list(map(int, sys.stdin.readline().split()))
board_future_max = first_line
board_future_min = first_line

for _ in range(n-1):
    now_line = list(map(int, sys.stdin.readline().split()))
    board_future_max = [max(board_future_max[0], board_future_max[1]) + now_line[0], max(board_future_max) + now_line[1], max(board_future_max[1], board_future_max[2]) + now_line[2]]
    board_future_min = [min(board_future_min[0], board_future_min[1]) + now_line[0], min(board_future_min) + now_line[1], min(board_future_min[1], board_future_min[2]) + now_line[2]]

print(max(board_future_max), min(board_future_min))