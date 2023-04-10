import sys

N = int(input())
cookie_body = list()
# 왼팔, 오른 팔, 허리, 왼다리, 오른다리
body_state = [0, 0, 0, 0, 0]

heart = [0, 0]
for _ in range(N):
    now_list = []
    now_line = sys.stdin.readline().rstrip()
    for now_part in now_line:
        now_list.append(now_part)
    cookie_body.append(now_list)

# print(cookie_body)

for i in range(N):
    for j in range(N):
        if cookie_body[i][j] == '*':
            if heart == [0, 0]:
                heart = [i + 1, j]
            else:
                if i == heart[0] and j != heart[1]:
                    if j < heart[1]:
                        body_state[0] += 1
                    elif j > heart[1]:
                        body_state[1] += 1
                elif i > heart[0]:
                    if j == heart[1]:
                        body_state[2] += 1
                    elif j < heart[1]:
                        body_state[3] += 1
                    elif j > heart[1]:
                        body_state[4] += 1

print(heart[0] + 1, heart[1]+ 1)
print(body_state[0], body_state[1], body_state[2], body_state[3], body_state[4])

        