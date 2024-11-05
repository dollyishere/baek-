def solution(my_string, num1, num2):
    answer = ''
    small, big = num1, num2
    if num1 > num2:
        small = num2
        big = num1
    
    save = my_string[small]

    answer = my_string[:small] + my_string[big] + my_string[small+1:big] + save
    
    if big < len(my_string):
        answer +=  my_string[big+1:]
    
    return answer