t = int(input())

for _ in range(t):
    n = int(input())
    now_sticker = []
    for _ in range(2):
        now_sticker.append(list(map(int, input().split())))

    sticker_memo = [[0] * 2 for _ in range(n+2)]
    
    for i in range(2, n+2):
        sticker_memo[i][0] = max(sticker_memo[i-1][1], sticker_memo[i-2][1]) + now_sticker[0][i-2]
        sticker_memo[i][1] = max(sticker_memo[i-1][0], sticker_memo[i-2][0]) + now_sticker[1][i-2]
    
    print(max(sticker_memo[n+1]))