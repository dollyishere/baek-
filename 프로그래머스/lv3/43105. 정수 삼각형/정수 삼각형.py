def solution(triangle):
    answer = 0
    height_t = len(triangle)
    dp = []
    for i in range(0, height_t):
        dp.append([0] * (i+1))
    
    dp[0][0] = triangle[0][0]
    
    for now_h in range(1, height_t):
        for now_w in range(now_h+1):
            if now_w == 0:
                dp[now_h][now_w] = dp[now_h-1][now_w] + triangle[now_h][now_w]
            elif now_w == now_h:
                dp[now_h][now_w] = dp[now_h-1][now_w-1] + triangle[now_h][now_w]
            else:
                dp[now_h][now_w] = max(dp[now_h-1][now_w], dp[now_h-1][now_w-1]) + triangle[now_h][now_w]
    
    answer = max(dp[height_t-1])
    return answer