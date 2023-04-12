import sys

def dfs(now_list, my_cards, max_list):
    if len(my_cards) == 3:
        max_list.append(int(str(now_list[my_cards[0]] + now_list[my_cards[1]] + now_list[my_cards[2]])[-1]))
    else:
        for i in range(5):
            if i not in my_cards:
                my_cards.append(i)
                dfs(now_list, my_cards, max_list)
                my_cards.pop()

N = int(sys.stdin.readline())
cards_state = list(list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N))
plus_list = [0] * N
for n in range(N):
    max_list = []
    dfs(cards_state[n], [], max_list)
    plus_list[n] = max(max_list)

max_num = max(plus_list)

max_people = 0
for n in range(N):
    if plus_list[n] == max_num:
        max_people = n

print(max_people + 1)