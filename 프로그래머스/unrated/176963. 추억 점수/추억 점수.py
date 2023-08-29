def solution(name, yearning, photo):
    answer = []
    
    for now_photo in photo:
        now_score = 0
        for now_person in now_photo:
            if now_person in name:
                now_score += yearning[name.index(now_person)]
        answer.append(now_score)
    return answer