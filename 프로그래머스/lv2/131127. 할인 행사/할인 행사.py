def solution(want, number, discount):
    answer = 0
    buy_list = []
    
    
    for day in range(len(discount)):
        wish_item_dict = dict()
        buy_list.append(discount[day])
        if len(buy_list) > 10:
            buy_list.pop(0)
        
        for i in range(len(want)):
            wish_item = want[i]
            wish_item_dict[wish_item] = number[i]
        
        for buy_item in buy_list:
            if buy_item in want:
                if wish_item_dict[buy_item] > 0:
                    wish_item_dict[buy_item] -= 1
                    
        if sum(wish_item_dict.values()) == 0:
            answer += 1

    return answer