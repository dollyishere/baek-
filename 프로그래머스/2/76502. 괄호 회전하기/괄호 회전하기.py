def check_right(check_s):
    s_dict = {
        "]" : "[",
        ")" : "(",
        "}" : "{"
    }
    
    stack = []
    
    for single_s in check_s:
        if stack:
            if single_s in s_dict and stack[-1] == s_dict[single_s]:
                stack.pop()
            else:
                stack.append(single_s)
        else:
            stack.append(single_s)
            
    if stack == []:
        return 1
    else:
        return 0
        

def solution(s):
    answer = 0
    for i in range(len(s)):
        answer += check_right(s)
        s = s[1:] + s[0]
    return answer