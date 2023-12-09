n = int(input())

tp_list = []
memo = [0] * (n+1)

for _ in range(n):
    tp_list.append(list(map(int, input().split())))

tp_list.reverse()
tp_list.insert(0, [])

for i in range(1, n+1):
    if i < tp_list[i][0]:
        memo[i] = memo[i-1]
    else:
        memo[i] = max(memo[i-1], tp_list[i][1] + memo[i - tp_list[i][0]])

print(memo[n])