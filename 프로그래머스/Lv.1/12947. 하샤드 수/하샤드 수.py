def solution(x):
    answer = True
    
    xs = str(x)
    num = 0
    
    for i in xs:
        num += int(i)
        
    if x % num != 0:
        answer = False
    
    return answer