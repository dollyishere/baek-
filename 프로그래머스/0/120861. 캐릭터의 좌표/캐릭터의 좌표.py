def solution(keyinput, board):
    answer = [0, 0]
    x, y = (board[0] // 2), (board[1] // 2)
    key_dict = {
        "left": [-1, 0],
        "right": [1, 0],
        "up": [0, 1],
        "down": [0, -1]
    }
    
    for key in keyinput:
        now_input = key_dict[key]
        
        answer[0] += now_input[0]
        answer[1] += now_input[1]
        
        if answer[0] > x:
            answer[0] = x
        elif answer[0] < -x:
            answer[0] = -x
            
        if answer[1] > y:
            answer[1] = y
        elif answer[1] < -y:
            answer[1] = -y
        
    return answer