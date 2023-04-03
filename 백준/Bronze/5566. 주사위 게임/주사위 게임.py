import sys

N, M = map(int, sys.stdin.readline().split())
order_list = list(int(sys.stdin.readline()) for _ in range(N))
dice_list = list(int(sys.stdin.readline()) for _ in range(M))

my_state = 1
move_cnt = 0

for m in range(M):
    move_cnt += 1
    my_state += dice_list[m]
    if dice_list[m] != 0:
        if 0 < my_state < N and order_list[my_state - 1] != 0:
            my_state += order_list[my_state - 1]
    if my_state >= N:
        print(move_cnt)
        break