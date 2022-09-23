T = int(input())

for tc in range(1, T+1):
    day, month, t_month, year = map(int, input().split())
    yearly_plan = list(map(int, input().split()))
    check = [0] * 12
    dp = [0] * 12
    answer = 0

    for y in range(12):
        if day * yearly_plan[y] < month:
            check[y] = day * yearly_plan[y]
        else:
            check[y] = month
    
    dp[0] = check[0]
    dp[1] = check[0] + check[1]
    dp[2] = min(sum(check[0:3]), t_month)

    for i in range(3, 12):
        dp[i] = min(check[i] + dp[i-1], dp[i-3] + t_month)
    # print(check)
    if dp[-1] > year:
        answer = year
    else:
        answer = dp[-1]


    print('#{} {}'.format(tc, answer))