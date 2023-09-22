def solution(picks, minerals):
    answer = 0
    
    picks_num = []
    minerals_set = []
    now_m_set = []
    cnt = 0
    
    if len(minerals) > sum(picks)*5:
        minerals = minerals[:sum(picks)*5]

    for now_n in range(len(minerals)):
        now_m_set.append(minerals[now_n])
        if len(now_m_set) == 5 or now_n == len(minerals) - 1:
            new_list = [0, 0, 0]
            for now_m in range(len(now_m_set)):
                if now_m_set[now_m] == "diamond":
                    new_list[0] += 1
                elif now_m_set[now_m] == "iron":
                    new_list[1] += 1
                else:
                    new_list[2] += 1                            
                
            minerals_set.append(new_list)
            now_m_set = []
    
    minerals_set.sort(key=lambda x:(-x[0],-x[1],-x[2]))

    now_pick = "diamond"
    for mineral in minerals_set:
        if picks[0]:
            picks[0] -= 1
            now_pick = "diamond"
        elif picks[1]:
            picks[1] -= 1
            now_pick = "iron"
        else:
            picks[2] -= 1
            now_pick = "stone"
        
        if now_pick == "diamond":
            answer += sum(mineral)
        elif now_pick == "iron":
            answer += (mineral[0]*5+mineral[1]+mineral[2])
        else:
            answer += (mineral[0]*25+mineral[1]*5+mineral[2])
            
    return answer