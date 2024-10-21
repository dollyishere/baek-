def solution(my_string):
    answer = list()
    
    for s in my_string:
        answer.append(s.lower())
        
    return "".join(sorted(answer))