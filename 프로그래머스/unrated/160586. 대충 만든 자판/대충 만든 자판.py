def solution(keymap, targets):
    answer = []
    for target in targets:
        pushing_number = 0
        impossible = False
        for word in target:
            short = 101
            for key in keymap:
                if key.find(word) < short and key.find(word) != -1:
                    short = key.find(word)
            if short == 101:
                impossible = True
                break
            else:
                pushing_number += (short + 1)
        if impossible:
            answer.append(-1)
        else:
            answer.append(pushing_number)
                
    return answer