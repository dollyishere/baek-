def solution(n, words):
    answer = [0, 0]
    last_words = [words[0]]
    
    # 현재 턴
    now_turn = 1
    # 현재 사람 번호
    now_p = 2
    # 지난 글자 마지막 단어
    past_word = words[0][-1]
    
    for t in range(1, len(words)):
        now_word = words[t]
        # 앞 글자가 앞 사람이 말한 단어의 마지막 문자이고, 이미 말한 단어가 아니라면
        if (now_word[0] == past_word) and (now_word not in last_words):
            # past_word 현재 단어 맨 끝 단어로 대체
            past_word = now_word[-1]
            # 지난 단어들 목록에 추가
            last_words.append(now_word)
            # 현재 사람 번호가 마지막이면 turn 하나씩 올리고 번호 리셋
            # 아니면 사람 번호 그냥 추가
            if now_p == n:
                now_p = 1
                now_turn += 1
            else:
                now_p += 1
        
        # 정답일 시, 탈락한 사람 번호와 현재 턴 값 넣고 break
        else:
            answer = [now_p, now_turn]
            break
    
    return answer