def solution(survey, choices):
    answer = ''
    chara_case = {"R": 0, "C": 0, "J": 0, "A": 0, "T": 0, "F": 0, "M": 0, "N": 0}
    a_case = ["R", "C", "J", "A", "T", "F", "M", "N"]
    
    for now_choice in range(len(survey)):
        now_down, now_up = survey[now_choice][0], survey[now_choice][1]
        now_score = choices[now_choice] - 4
        if now_score < 0:
            chara_case[now_down] += abs(now_score)
        elif now_score > 0:
            chara_case[now_up] += now_score
            
    for i in range(4):
        first_case = chara_case[a_case[i]]
        second_case = chara_case[a_case[i+4]]
        if first_case > second_case:
            answer += a_case[i]
        elif first_case < second_case:
            answer += a_case[i+4]
        else:
            answer += sorted([a_case[i],a_case[i+4]])[0]
    
    return answer