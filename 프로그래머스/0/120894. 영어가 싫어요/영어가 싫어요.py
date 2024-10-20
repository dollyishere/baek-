def solution(numbers):
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
        "nine" : 9,
    }
    
    num_s = ""  
    answer = ""
    
    for number in numbers:
        num_s += number
        if num_s in num_dict:
            answer += str(num_dict[num_s])
            num_s = ""
            
    return int(answer)