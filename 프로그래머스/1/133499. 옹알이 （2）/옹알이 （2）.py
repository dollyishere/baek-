def solution(babbling):
    answer = 0
    can_talk = ["aya", "ye", "woo", "ma"]
    
    for bab in babbling:
        now_case_good = True
        pre_bab = ""
        now_bab = ""
        for b in range(len(bab)):
            now_bab += bab[b]
            # print(pre_bab, now_bab)
            if len(now_bab) == 2:
                if now_bab in can_talk and now_bab != pre_bab:
                    pre_bab = now_bab
                    now_bab = ""
            if len(now_bab) >= 3:
                if now_bab in can_talk and now_bab != pre_bab:
                    pre_bab = now_bab
                    now_bab = ""
                else:
                    now_case_good = False
                    break
        if now_bab == "" and now_case_good:
            answer += 1
    return answer
