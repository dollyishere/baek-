def solution(cards1, cards2, goal):
    answer = 'Yes'
    card_one = 0
    card_two = 0
    for word in goal:
        print(word)
        if (word in cards1) and (cards1.index(word) == card_one):
            card_one += 1
        elif (word in cards2) and (cards2.index(word) == card_two):
            card_two += 1
        else:
            answer = 'No'
            break
            
    return answer