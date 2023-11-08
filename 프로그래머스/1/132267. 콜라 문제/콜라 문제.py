def solution(a, b, n):
    answer = 0
    now_coke = n
    while True:
        if now_coke < a:
            break
        can_get = now_coke // a
        answer += can_get * b
        now_coke %= a
        now_coke += can_get * b
        
        
    return answer