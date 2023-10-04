def solution(elements):
    answer = 0
    num_set = set()
    how_long = len(elements)
    elements *= 2
    for i in range(1, how_long+1):
        for j in range(how_long):
            num_set.add(sum(elements[j:i+j]))
            
    return len(num_set)