def solution(arr):
    answer = []
    last_a = ""
    for a in arr:
        if a != last_a:
            answer.append(a)
        last_a = a
    return answer