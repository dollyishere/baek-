def solution(i, j, k):
    answer = 0
    
    for s in range(i, j+1):
        for n in str(s):
            if str(k) == n:
                answer += 1

    return answer