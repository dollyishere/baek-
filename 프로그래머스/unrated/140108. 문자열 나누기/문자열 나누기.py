def solution(s):
    answer = 0
    
    # 첫번째 단어 slicing
    first_word = s[0]
    first_word_count = 0
    another_word_count = 0
    cnt = 0
    words = ''
    
    for word in s:
        cnt += 1
        words += word
        if first_word_count == 0:
            first_word = word
            
        if word == first_word:
            first_word_count += 1
        else:
            another_word_count += 1
        
        if first_word_count == another_word_count:
            answer += 1
            first_word_count = 0
            another_word_count = 0
        elif cnt == len(s):
            answer += 1
    
    return answer