def solution(n, lost, reserve):
    answer = 0
    check_dict = dict()
    can_parti = []
    
    for i in range(1, n+1):
        check_dict[i] = 1
        if i in reserve:
            check_dict[i] += 1
        if i in lost:
            check_dict[i] -= 1

    for i in range(1, n+1):
        now_s = check_dict[i]
        if now_s >= 1:
            check_dict[i] -= 1
            can_parti.append(i)
        else:
            if i > 1 and check_dict[i-1]:
                check_dict[i-1] -= 1
                can_parti.append(i)
            elif i != n and check_dict[i+1] > 1:
                check_dict[i+1] -= 1
                can_parti.append(i)

    answer = len(can_parti)
                
    return answer