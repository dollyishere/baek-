n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

answer = []
def back_track(start, now):
    if now == m:
        print(*answer)
        return
    else:
        for i in range(start, n):
            answer.append(nums[i])
            back_track(i, now+1)
            answer.pop()

back_track(0, 0)
