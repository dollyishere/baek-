def solution(my_string):
    answer = 0
    num = ""
    for s in my_string:
        if s.isdigit():
            num += s
        else:
            if len(num) != 0:
                answer += int(num)
                num = ""
            
    if len(num) != 0:
        answer += int(num)
    
    return answer