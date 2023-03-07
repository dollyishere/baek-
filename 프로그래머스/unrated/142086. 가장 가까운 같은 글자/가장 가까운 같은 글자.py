def solution(s):
    answer = []
    for num in range(len(s)):
        now_word = s[num]
        if num == 0:
            answer.append(-1)
        else:
            word_cnt = 0
            for back_num in range(num - 1, -1, -1):
                word_cnt += 1
                if s[back_num] == now_word:
                    answer.append(word_cnt)
                    break
                elif word_cnt == num:
                    answer.append(-1)

    return answer