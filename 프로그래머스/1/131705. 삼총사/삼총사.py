def solution(number):
    answer = 0
    stack = []
    not_visited = [True for _ in range(len(number))]
    
    def dfs(stack, not_visited):
        nonlocal answer
        if len(stack) == 3:
            if sum(stack) == 0:
                answer += 1         
        else:
            for num in range(len(number)):
                if not_visited[num]:
                    not_visited[num] = False
                    stack.append(number[num])
                    dfs(stack, not_visited)
                    stack.pop()
                    not_visited[num] = True
    
    for num in range(len(number)):
        not_visited[num] = False
        dfs([number[num]], not_visited)
    
    return answer // 2