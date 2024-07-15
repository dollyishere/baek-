def solution(s):
    now_first = True
    answer = ''
    
    for i in range(len(s)):
        if s[i] == " ":
            now_first = True
            answer += s[i]
            continue
            
        if now_first:
            if s[i].isalpha():
                answer += s[i].upper()
            else:
                answer += s[i]
            now_first = False
        else:
            answer += s[i].lower()
    
    return answer