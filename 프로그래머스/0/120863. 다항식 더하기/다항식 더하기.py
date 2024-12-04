def solution(polynomial):
    answer = ""
    p_list = list(polynomial.split())
    num = 0
    x_num = 0
    
    for p in p_list:
        if p.isdigit():
            num += int(p)
        
        if p[-1] == "x":
            new_x = p[:len(p)-1]
            if len(p) == 1:
                new_x = 1
            x_num += int(new_x)
            
    if x_num == 1:
        answer += "x"
    elif x_num > 1:
        answer += str(x_num) + "x"
    
    if num > 0:
        if len(answer) == 0:
            answer += str(num)
        else:
            answer += " + " + str(num)
    
    return answer