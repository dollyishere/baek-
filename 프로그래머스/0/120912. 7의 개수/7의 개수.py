def solution(array):
    answer = 0
    
    for a in array:
        for i in range(len(str(a))):
            if str(a)[i] == "7":
                answer += 1
                
    return answer