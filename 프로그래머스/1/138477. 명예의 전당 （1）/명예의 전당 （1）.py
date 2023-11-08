def solution(k, score):
    answer = []
    legend = []
    for today_s in score:
        if len(legend) < k:
            legend.append(today_s)
        else:
            if legend[-1] < today_s:
                legend.pop()
                legend.append(today_s)
        legend.sort(reverse=True)
        answer.append(legend[-1])
        
    return answer