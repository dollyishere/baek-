n = int(input())
tri_state = []
for _ in range(n):
    tri_state.append(list(map(int, input().split())))

tri_add = []

for i in range(1, n+1):
    tri_add.append([0] * i)

tri_add[0][0] = tri_state[0][0]

for i in range(n-1):
    for j in range(i+1):
        if tri_add[i+1][j] < tri_add[i][j] + tri_state[i+1][j]:
            tri_add[i+1][j] = tri_add[i][j] + tri_state[i+1][j]
        if tri_add[i+1][j+1] < tri_add[i][j] + tri_state[i+1][j+1]:
            tri_add[i+1][j+1] = tri_add[i][j] + tri_state[i+1][j+1]

print(max(tri_add[n-1]))