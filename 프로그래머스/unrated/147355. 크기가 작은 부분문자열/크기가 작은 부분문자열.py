def solution(t, p):
    answer = 0
    start, end = 0, len(p)
    while True:
        if end == len(t)+1:
            break
        if int(t[start:end]) <= int(p):
            answer += 1
        start += 1
        end += 1
        
    return answer