from collections import deque

def solution(x, y, n):
    answer = 0
    check = [0 for _ in range(y+1)]
    queue = deque()
    queue.append(x)
    trigger = True
    
    if x == y:
        return 0
    while queue:
        if trigger == False:
            break
        pre_x = queue.popleft()
        
        for i in range(3):
            if i == 0:
                now_x = pre_x + n
            elif i == 1:
                now_x = pre_x * 2
            elif i == 2:
                now_x = pre_x * 3

            if now_x < y:
                if check[now_x] == 0:
                    check[now_x] = check[pre_x] + 1
                    queue.append(now_x)
            if now_x == y:
                if check[now_x] == 0:
                    check[y] = check[pre_x] + 1
                    trigger = False
                    break
                
    if x != y and check[y] == 0:
        answer = -1
    else:
        answer = check[-1]
        
    return answer