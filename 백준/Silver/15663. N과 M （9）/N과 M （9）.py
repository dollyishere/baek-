import copy

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [False] * n
answer = []
tem = []

def back_track(now, arr):
    global answer
    if now == m:
        new_list = arr.copy()
        answer.append(new_list)
        return
    else:
        for i in range(n):
            if visited[i] == False:
                arr.append(nums[i])
                visited[i] = True
                back_track(now+1, arr)
                arr.pop()
                visited[i] = False

back_track(0, [])
answer = sorted(list(set(map(tuple, answer))))
for i in answer:
    print(*i)