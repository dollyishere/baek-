def solution(s, skip, index):
    answer = ''
    for now_word in s:
        now_word_int = ord(now_word)
        check_cnt = 0
        
        while check_cnt < index:
            now_word_int += 1
            # a~z 범위 벗어났을 시 예외처리
            if now_word_int == ord("z") + 1:
                now_word_int = ord("a")
            if chr(now_word_int) not in skip:
                check_cnt += 1
        answer += chr(now_word_int)
        
    return answer