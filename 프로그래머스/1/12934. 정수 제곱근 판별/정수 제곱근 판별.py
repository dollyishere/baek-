def solution(n):
    answer = -1
       
    for i in range(1, n//2+1):
        if n / i == i and n % i == 0:
            print(i)
            answer = (i + 1) ** 2
            break
    
    if n == 1:
        answer = 4
    
    return answer