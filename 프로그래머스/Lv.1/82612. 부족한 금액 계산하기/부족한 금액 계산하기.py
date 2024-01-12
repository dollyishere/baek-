def solution(price, money, count):
    answer = 0
    now_p = 0
    for c in range(1, count+1):
        now_p += (price * c)
    
    if now_p > money:
        answer = now_p - money

    return answer