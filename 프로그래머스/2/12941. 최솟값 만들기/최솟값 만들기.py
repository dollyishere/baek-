def solution(A,B):
    answer = 0

    A.sort()
    B.sort(reverse=True)
    
    for n in range(len(A)):
        answer += A[n] * B[n]

    return answer