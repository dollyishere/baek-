def solution(arr):
    answer = arr
    low = arr.index(min(arr))
    answer.pop(low)
    if answer == []:
        answer = [-1]
    return answer