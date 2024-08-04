def solution(s):
    answer = True
    
    cnt_p = s.count('p')
    cnt_p += s.count('P')
    cnt_y = s.count('y')
    cnt_y += s.count('Y')
    
    if cnt_p != cnt_y:
        return False
    return True