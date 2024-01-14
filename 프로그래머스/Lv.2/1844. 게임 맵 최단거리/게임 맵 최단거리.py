from pprint import pprint

def solution(maps):
    answer = -1
    n, m = len(maps), len(maps[0])
    meta = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    
    i_here = [0, 0, 1]
    visited = [[True] * m for _ in range(n)]
    queue = [i_here]
    visited[0][0] = False
    
    while queue:
        now_here = queue.pop(0)
        for k in range(4):
            di = now_here[0] + meta[k][0]
            dj = now_here[1] + meta[k][1]
            if 0 <= di < n and 0 <= dj < m and maps[di][dj] and visited[di][dj]:
                if [di, dj] == [n-1, m-1]:
                    visited[di][dj] = False
                    answer = now_here[2] + 1
                    break
                else:
                    visited[di][dj] = False
                    queue.append([di, dj, now_here[2]+1])
    pprint(visited)               
    return answer