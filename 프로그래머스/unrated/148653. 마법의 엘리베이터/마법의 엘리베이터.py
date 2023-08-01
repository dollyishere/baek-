def solution(storey):
    # -층으로는 이동 불가
    # 단위는 10씩?
    # bfs? 그리디?
    # 5 이상부터는 그냥 더해서 나누는 게 더 나음
    # 5 미만일 시에는 빼는 게 더 이득임
    
    answer = 0
    while storey:
        print(storey)
        now_num = storey % 10
        storey //= 10
        if now_num > 5:
            answer += (10 - now_num)
            storey += 1
        elif now_num < 5:
            answer += now_num
        else:
            if (storey % 10 + 1) > 5:
                answer += (10 - now_num)
                storey += 1
            else:
                answer += now_num
    return answer