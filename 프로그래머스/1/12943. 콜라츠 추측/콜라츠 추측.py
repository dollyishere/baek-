def solution(num):
    answer = 0
    if num == 0:
        pass
    else:
        cnt = 0
        while True:
            if num == 1 or cnt > 500:
                break
            cnt += 1
            if num % 2 == 0:
                num //= 2
            elif num % 2 == 1:
                num = num * 3 + 1
        if cnt > 500:
            answer = -1
        else:
            answer = cnt
    return answer