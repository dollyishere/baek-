import sys

N = int(sys.stdin.readline())
data = []
now_time = 0

for n in range(N):
    arrival, check_time = map(int, sys.stdin.readline().split())
    data.append([arrival, check_time])

data.sort()

for n in range(N):
    arrival, check_time = data[n][0], data[n][1]
    if now_time < arrival:
        now_time = arrival
    now_time += check_time

print(now_time)
