def solution(emergency):
    answer = []
    sort_emergency = sorted(emergency, reverse=True)

    for emer in emergency:
        answer.append(sort_emergency.index(emer) + 1)
    return answer