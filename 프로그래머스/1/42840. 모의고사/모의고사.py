def solution(answers):
    score_dict = dict()
    
    score_dict[1] = 0
    score_dict[2] = 0
    score_dict[3] = 0
    
    score_pattern = dict()
    
    score_pattern[1] = "12345"
    score_pattern[2] = "21232425"
    score_pattern[3] = "3311224455"
    
    for i in score_dict:
        cnt = 0
        now_pattern = score_pattern[i]
        for a in answers:
            if a == int(now_pattern[cnt]):
                score_dict[i] += 1
            cnt += 1
            if cnt == len(now_pattern):
                cnt = 0
    
    total_score = list()
    for j in score_dict:
        total_score.append(score_dict[j])
    
    max_score = max(total_score)
    
    answer = []
    
    for n in range(3):
        if total_score[n] == max_score:
            answer.append(n+1)     
    
    return answer