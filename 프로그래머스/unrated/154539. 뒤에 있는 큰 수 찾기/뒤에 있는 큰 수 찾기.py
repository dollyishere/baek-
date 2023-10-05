def solution(numbers):
    answer = [0] * len(numbers) 
    stack = []
    
    for num in range(len(numbers)):
        while stack:
            if stack[-1][1] < numbers[num]:
                now_n = stack.pop()
                answer[now_n[0]] = numbers[num]
            else:
                break
        stack.append([num, numbers[num]])
    
    while stack:
        now_n = stack.pop()
        answer[now_n[0]] = -1
        
    return answer