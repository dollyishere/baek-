def solution(s):
    answer = ""
    num_s = ""
    
    num_dict = {
        "zero" : 0,
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9
    }
    
    for i in s:
        if i.isdigit():
            if num_s != "":
                answer += str(num_dict[num_s])
                num_s = ""
            answer += i
        else:
            num_s += i
            if num_s in num_dict:
                answer += str(num_dict[num_s])
                num_s = ""
    if num_s != "":
        answer += num_dict[num_s]
    
    return int(answer)