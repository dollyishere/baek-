def solution(maps):
    answer = []
    not_v = [[True] * len(maps[0]) for _ in range(len(maps))]
    moving = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                
    for x in range(len(maps)):
        for y in range(len(maps[x])):
            if maps[x][y] != 'X' and not_v[x][y]:
                island_list = []
                island_cnt = 0
                island_list.append([x, y])
                island_cnt += int(maps[x][y])
                not_v[x][y] = False
                
                while island_list:
                    now_land = island_list.pop(0)
                    for k in range(4):
                        di = now_land[0] + moving[k][0]
                        dj = now_land[1] + moving[k][1]
                        if 0 <= di < len(maps) and 0 <= dj < len(maps[0]) and maps[di][dj] != "X" and not_v[di][dj]:
                            island_list.append([di, dj])
                            island_cnt += int(maps[di][dj])
                            not_v[di][dj] = False
                answer.append(island_cnt)
                
    if not answer:
        answer = [-1]
    else:
        answer.sort()
        
    return answer