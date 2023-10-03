def solution(weights):
    answer = 0
    weights.sort()
    weight_dict = dict()
    
    for weight in weights:
        one_w = weight
        two_w = weight * 2 / 3
        three_w = weight * 2 / 4
        four_w = weight * 3 / 4
        
        if one_w in weight_dict:
            answer += weight_dict[one_w]
        if two_w in weight_dict:
            answer += weight_dict[two_w]
        if three_w in weight_dict:
            answer += weight_dict[three_w]
        if four_w in weight_dict:
            answer += weight_dict[four_w]
        
        # 같은 몸무게를 가진 사람이 여럿 존재할 수 있으므로, 값 존재 시 1씩 더해줌
        if one_w in weight_dict:
            weight_dict[one_w] += 1
        else:
            weight_dict[one_w] = 1
        
    return answer