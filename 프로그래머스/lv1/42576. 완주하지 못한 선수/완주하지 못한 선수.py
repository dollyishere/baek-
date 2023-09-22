def solution(participant, completion):
    answer = ''
    completions_dict = {}
    completions = []
    
    for part in participant:
        if part not in completions_dict:
            completions_dict[part] = 1
        else:
            completions_dict[part] += 1

    for com in completion:
        completions_dict[com] -= 1
    
    for now_com in completions_dict:
        if completions_dict[now_com] != 0:
            answer = now_com
            break
            
    return answer