N = int(input())
students = [list(map(int, input().split())) for _ in range(N)]
check = [[] for _ in range(N)]

for i in range(N):
    student = i
    for j in range(N):
        if j == i:
            pass
        else:
            for y in range(5):
                if students[i][y] == students[j][y] and j not in check[i]:
                    check[i].append(j)
                    break

maxv = 0
for c in range(N):
    if len(check[c]) > len(check[maxv]):
        maxv = c

print(maxv + 1)


