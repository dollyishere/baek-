def solution(s):
    answer = True
    
    stack = []
    
    for now_s in s:
        if stack == [] and now_s == ')':
            answer = False
            break
    
        if stack:
            if now_s == stack[-1]:
                stack.append(now_s)
            else:
                stack.pop()
        else:
            stack.append(now_s)
    
    if stack:
        answer = False

    return answer