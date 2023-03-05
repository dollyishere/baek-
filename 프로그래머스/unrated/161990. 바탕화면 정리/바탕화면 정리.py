def solution(wallpaper):
    answer = []
    f_left, f_right, l_left, l_right = 51, 51, 0, 0
    x_cnt = 0
    
    for w_line in wallpaper:
        y_cnt = 0
        for item in w_line:
            if item == '#':
                if f_left == 51:
                    f_left = x_cnt
                if y_cnt < f_right:
                    f_right = y_cnt
                if l_left < x_cnt:
                    l_left = x_cnt
                if l_right < y_cnt:
                    l_right = y_cnt
            y_cnt += 1
        x_cnt += 1
        
    answer = [f_left, f_right, l_left+1, l_right+1]
    return answer