def solution(array, commands):
    answer = []
    
    for command in commands:
        i, j, k = command
        array_copy = array[i-1:j]
        array_copy.sort()
        answer.append(array_copy[k-1])
        
    return answer