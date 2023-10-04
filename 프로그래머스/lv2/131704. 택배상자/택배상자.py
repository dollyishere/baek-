def solution(order):
    # 스택 문제
    answer = 0
    truck = []
    stack = []
    
    now_cnt = 0
    
    for i in range(1, len(order)+1):
        if i == order[now_cnt]:
            truck.append(i)
            now_cnt += 1
            while stack:
                if stack[-1] == order[now_cnt]:
                    truck.append(stack.pop())
                    now_cnt += 1
                else:
                    break
        else:
            stack.append(i)
            
    while stack:
        if stack[-1] == order[now_cnt]:
            truck.append(stack.pop())
            now_cnt += 1
        else:
            break
        
    return len(truck)