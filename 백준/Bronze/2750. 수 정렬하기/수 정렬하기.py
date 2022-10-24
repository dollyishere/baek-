N = int(input())
num_list = [int(input()) for _ in range(N)]

for i in range(N - 1):
    minv = i
    for j in range(i+1, N):
        if num_list[minv] > num_list[j]:
            minv = j
    num_list[minv], num_list[i] = num_list[i], num_list[minv]

for n in range(N):
    print(num_list[n])