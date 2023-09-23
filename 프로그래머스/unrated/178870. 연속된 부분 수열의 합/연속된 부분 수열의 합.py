def solution(sequence, k):
    answer = []
    start, end = 0, -1
    now_sum = 0
    min_len = 10000001
    
    while True:
        if now_sum < k:
            end += 1
            if end >= len(sequence):
                break
            now_sum += sequence[end]
        else:
            now_sum -= sequence[start]
            if start >= len(sequence):
                break
            start+= 1
            
        if now_sum == k:
            answer.append([start, end])

    answer.sort(key=lambda x : (x[1]-x[0], x[0]))
    return answer[0]