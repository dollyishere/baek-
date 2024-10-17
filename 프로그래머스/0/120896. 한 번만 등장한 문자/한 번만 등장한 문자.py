def solution(s):
    answer = []
    s_dict = dict()
    
    for now_s in s:
        if now_s not in s_dict:
            s_dict[now_s] = 1
        else:
            s_dict[now_s] += 1
    
    
    for i in s_dict:
        if s_dict[i] == 1:
            answer.append(i)

    return "".join(sorted(answer))