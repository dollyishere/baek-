def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    start, end = 0, len(people)-1
    while True:
        if end <= start or end < 0 or start == len(people):
            break
        else:
            now_max = people[start] + people[end]
            if now_max > limit:
                start += 1
            else:
                people[start], people[end] = 0, 0
                start += 1
                end -= 1
                answer += 1
    
    for p in people:
        if p:
            answer += 1
    return answer