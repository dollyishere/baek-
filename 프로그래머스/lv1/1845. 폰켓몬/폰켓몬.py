def solution(nums):
    answer = 0
    can_get = len(nums) // 2
    nums = set(nums)
    
    if can_get > len(nums):
        answer = len(nums)
    else:
        answer = can_get
    return answer