def solution(n):
    answer = 0
    num_list = []
    
    for i in str(n):
        num_list.append(i)
    num_list.sort(reverse=True)
    answer = int("".join(num_list))
    return answer