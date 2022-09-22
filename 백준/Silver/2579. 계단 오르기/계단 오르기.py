def max_i(x, y):
    if x > y:
        return x
    else:
        return y

N = int(input())
stairs = [int(input()) for _ in range(N)]
dp = [0] * N
answer = 0

if N >= 3:
    dp[0] = stairs[0]
    dp[1] = max_i(stairs[1], stairs[0] + stairs[1])
    dp[2] = max_i(stairs[0] + stairs[2], stairs[1] + stairs[2])

    if N >3:
        for i in range(3, N):
            dp[i] = max_i(stairs[i] + dp[i - 2], stairs[i] + stairs[i - 1] + dp[i - 3])
    print(dp[-1])
else:
    print(sum(stairs))