def solution(k, tangerine):
    answer = 0

    tan_dict = dict()
    
    for t in tangerine:
        if t in tan_dict:
            tan_dict[t] += 1
        else:
            tan_dict[t] = 1
    
    tan_dict = dict(sorted(tan_dict.items(), key=lambda x: x[1], reverse=True))
    
    for tang in tan_dict:
        if k <= 0:
            break
        k -= tan_dict[tang]
        answer += 1

    return answer