n, m = map(int, input().split())
nums = sorted(list(set(map(int, input().split()))))

def back_track(now, arr, prev):
    if now == m:
        print(*arr)
        return
    else:
        for i in range(prev, len(nums)):
            arr.append(nums[i])
            back_track(now+1, arr, i)
            arr.pop()

back_track(0, [], 0)