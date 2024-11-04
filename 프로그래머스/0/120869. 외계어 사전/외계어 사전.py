from copy import deepcopy

def solution(spell, dic):
    answer = 2
    check_spell = dict()
    
    for s in spell:
        check_spell[s] = 0
        
    for now_dict in dic:
        now_check = deepcopy(check_spell)
        
        for d in now_dict:    
            if d not in spell:
                break
            elif now_check[d] >= 1:
                break
            else:
                now_check[d] += 1
        
        if sum(now_check.values()) == len(spell):
            answer = 1
        
    return answer