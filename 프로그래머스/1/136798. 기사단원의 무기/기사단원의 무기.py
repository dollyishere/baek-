def solution(number, limit, power):
    answer = 1
    for n in range(2, number+1):
        cnt = 0
        for i in range(1, int(n**(1/2)+1)):
            if n % i == 0:
                cnt += 1
                if i ** 2 != n:
                    cnt += 1
        if cnt > limit:
            answer += power
        else:
            answer += cnt
    return answer