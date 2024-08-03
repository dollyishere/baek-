def solution(n):
    # 기본적으로 자기 자신 => 정답 조건에 들어가므로 1로 시작
    answer = 1
    
    for i in range(1, n+1):
        sum_n = i
        for j in range(i+1, n+1):
            sum_n += j
            if sum_n == n:
                answer += 1
                break
            elif sum_n > n:
                break
            
    return answer