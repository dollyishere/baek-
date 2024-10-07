def solution(s):
    s_list = list(s.split())
    pre_v = s_list[0]
    answer = int(pre_v)
    
    for i in range(1, len(s_list)):
        s_p = s_list[i]
        
        if s_p == "Z":
            answer -= int(pre_v)
        else:
            answer += int(s_p)
            pre_v = int(s_p)
    
    return answer