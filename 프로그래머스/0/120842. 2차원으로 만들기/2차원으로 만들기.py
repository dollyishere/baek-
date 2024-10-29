def solution(num_list, n):
    answer = list()
    cnt = 0
    mini = list()
    
    for num in num_list:
        mini.append(num)
        cnt += 1
        if cnt == n:
            answer.append(mini)
            mini = list()
            cnt = 0
            
    return answer