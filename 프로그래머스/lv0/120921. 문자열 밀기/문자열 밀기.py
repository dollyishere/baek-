def solution(A, B):
    answer = 0
    for a in range(len(A)+1):
        if A != B:
            answer += 1
            A = A[-1] + A[:-1]
            print(A)
        else:
            break
    if answer == len(A)+1:
        answer = -1
        
    return answer