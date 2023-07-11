import sys, math

n = int(input())
m = int(input())

bus_info = [[math.inf] * n for _ in range(n)]

# 노선의 경우, 단방향이며, 같은 도시를 오가도 방향이 다르면 가격이 달라짐
# 고로 단방향만 기록하면 ㅇㅋ
# 또, 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있으므로, 최소 값만 입력받아야 함
for _ in range(m):
    start_town, end_town, bus_charge = map(int, input().split())
    if bus_charge < bus_info[start_town-1][end_town-1]:
        bus_info[start_town-1][end_town-1] = bus_charge 

for k in range(n):
    for i in range(n):
        for j in range(n):
            if bus_info[i][j] > bus_info[i][k] + bus_info[k][j]:
                bus_info[i][j] = bus_info[i][k] + bus_info[k][j]

for i in range(n):
    for j in range(n):
        if i == j or bus_info[i][j] == math.inf:
            print(0, end=' ')
        else:
            print(bus_info[i][j], end=' ')
    print()
                