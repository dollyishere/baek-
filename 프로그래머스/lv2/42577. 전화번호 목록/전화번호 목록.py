def solution(phone_book):
    phone_book.sort(key=lambda x : x)
    answer = True
    for num in range(len(phone_book)-1):
        now_num = phone_book[num]
        next_num = phone_book[num+1]
        if len(now_num) > len(next_num):
            pass
        else:
            if now_num == next_num[:len(now_num)]:
                answer = False
                break
    return answer