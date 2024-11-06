def solution(numbers):
    answer = max(numbers)
    
    numbers.pop(numbers.index(max(numbers)))
    
    return answer * max(numbers)