def solution(cards):
    answer = 0
    answer_list = []
    count_over = False
    
    def first_card_game(first_num):
        global count_over
        find_first_num = False
        this_num = first_num
        find_cnt = 0
        find_num_list = []
        while find_cnt != len(cards):
            
            check_box = cards[this_num - 1]
            if check_box in find_num_list and len(find_num_list) != len(cards):
                find_first_num = True
                break
            else:
                find_num_list.append(check_box)
                this_num = check_box
                find_cnt += 1
            if len(find_num_list) == len(cards):
                count_over = True
                break
        return(this_num, find_num_list, find_cnt)
    
    def last_card_game(this_num, find_num_list, find_cnt):
        last_find_cnt = 0
        now_num = this_num
        find_now_num = False
        while find_now_num == False:
            
            check_box = cards[now_num - 1]
            if check_box in find_num_list:
                find_now_num = True
                break
            else:
                now_num = check_box
                find_num_list.append(check_box)
                last_find_cnt += 1
            if len(find_num_list) == len(cards):
                break
        return last_find_cnt
        

    for card in cards:
        this_num, find_num_list, find_cnt = first_card_game(card)
        if find_cnt == len(cards):
            answer_list.append(0)
        else:
            for card in cards:
                if card not in find_num_list:
                    last_find_cnt = last_card_game(card, find_num_list, find_cnt)
                    answer_list.append(last_find_cnt * find_cnt)
                    
    answer = max(answer_list)
    return answer