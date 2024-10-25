def solution(array, n):
    answer = array[0]
    
    for a in array:
        if abs(a - n) < abs(answer - n) or (abs(a-n) == abs(answer-n) and a < answer):
            answer = a
        
    return answer