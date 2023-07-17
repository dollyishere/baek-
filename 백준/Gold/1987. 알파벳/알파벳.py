# 백트래킹 문제...인데 이래도 되나...

r, c = map(int, input().split())

def back_track(i, j, now_route, cnt):
    global answer
    answer = max(answer, cnt)
    for k in range(4):
        di = i + moving[k][0]
        dj = j + moving[k][1]
        if 0 <= di < r and 0 <= dj < c and now_route[ord(alpha_list[di][dj])-65] != 1:
            now_route[ord(alpha_list[di][dj])-65] = 1
            cnt += 1
            back_track(di, dj, now_route, cnt)
            now_route[ord(alpha_list[di][dj])-65] = 0
            cnt -= 1
    
answer = 0
alpha_list = []
# 알파벳 수만큼 0을 지닌 visited_list 생성
visited_list = [0] * 26

moving = [[0, 1], [0, -1], [1, 0], [-1, 0]]

for _ in range(r):
    now_alpha = []
    now_line = input()
    for i in range(c):
        now_alpha.append(now_line[i])
    alpha_list.append(now_alpha)

# ord 함수로 대문자 알파벳을 유니코드로 변환 시 A=65이므로 65씩 빼준 인덱스 값을 1로 변경
visited_list[ord(alpha_list[0][0])-65] = 1
back_track(0, 0, visited_list, 1)
print(answer)
