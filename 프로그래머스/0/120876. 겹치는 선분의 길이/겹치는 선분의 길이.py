def solution(lines):
    lines = sorted(lines)
    part_dict = {}
    answer = 0
    
    for line in lines:
        for i in range(line[0], line[1]):
            part_dict[i] = part_dict.get(i, 0) + 1
    print(part_dict)
    for part in part_dict:
        if part_dict[part] >= 2:
            answer += 1
    return answer