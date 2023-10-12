def solution(progresses, speeds):
    answer = []
    stack = []
    
    days = 0
    now_new = 0
    
    while True:
        days += 1
        for p_c in range(len(progresses)):
            if progresses[p_c]:
                progresses[p_c] += speeds[p_c]
            if progresses[p_c] >= 100:
                stack.append(p_c)
                progresses[p_c] = 0
        
        stack.sort()
        out_list = []
        for s in range(len(stack)):
            if stack[s] == now_new:
                out_list.append(s)
                now_new += 1
            else:
                break

        if out_list:
            stack = stack[len(out_list):]
            answer.append(len(out_list))
        
        if sum(progresses) == 0 and stack == []:
            break
    
    return answer