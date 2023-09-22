import math

def solution(r1, r2):
    answer = 0
    # 원을 사분면으로 나눠서 계산함
    # ceil은 실수를 올림, floor는 실수를 내렴
    for i in range(1, r2+1):
        # 피타고라스 정리 
        h_r1 = math.sqrt(r2**2-i**2)
        h_r2 = 0 if i > r1 else math.sqrt(r1**2-i**2)
        answer += math.floor(h_r1) - math.ceil(h_r2) + 1
    
    return answer*4