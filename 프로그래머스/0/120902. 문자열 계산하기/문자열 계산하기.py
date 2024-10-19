def solution(my_string):
    my_string_list = list(my_string.split(" "))
    answer = int(my_string_list[0])
    pre = my_string_list[1]
    
    for i in range(2, len(my_string_list)):
        if i % 2 == 0:
            if pre == "+":
                answer += int(my_string_list[i])
            else:
                answer -= int(my_string_list[i])
        
        else:
            pre = my_string_list[i]
    return answer