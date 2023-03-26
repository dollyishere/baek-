def solution(food):
    answer = ''
    
    my_food = ''
    your_food = ''
    
    for now_food in range(len(food)):
        if food[now_food] // 2 > 0:
            my_food += str(now_food) * (food[now_food] // 2)
            your_food = str(now_food) * (food[now_food] // 2) + your_food
    
    answer = my_food + '0' + your_food
    return answer