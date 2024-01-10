def solution(numbers):
    num_list = [1] * 10
    answer = 0
    for n in numbers:
        num_list[n] = 0
    
    for num in range(10):
        if num_list[num]:
            answer += num
    return answer