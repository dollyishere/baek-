from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque([(0, 0)])
    
    while queue:
        n, l = queue.popleft()
        if l > len(numbers):
            break
        elif l == len(numbers) and n == target:
            answer += 1
        queue.append(([n+numbers[l-1], l+1]))
        queue.append(([n-numbers[l-1], l+1]))
            
    return answer