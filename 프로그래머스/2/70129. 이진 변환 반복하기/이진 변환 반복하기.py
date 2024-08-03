def solution(s):
    answer = [0, 0]
    
    # 해야 하는 것
    # 1. 문자열에서 0 빼기
    # 2. 문자열 길이 구하기
    # 3. 문자열 길이를 2진법으로 표현한 문자열로 바꾸기
    # 4. 문자열 길이가 1이 되면 break => 조건만 알지 반복 횟수가 정해진 건 아님(while)
    
    while True:
        # 1번 수행
        answer[1] += s.count("0")
        x = "".join(s.split("0"))
        answer[0] += 1
        
        # 탈출 조건(4번)
        if len(x) == 1:
            break
            
        # 3번 수행
        change_s = 0
        len_x = len(x)
        
        # 홀수일 때 1 더하고 시작
        if len_x % 2 != 0:
            change_s += 1
            len_x -= 1
            
        # 몫 초기값 지정
        po = 1
        
        # 2진법 전환 방법
        # po 값을 len_x // (2 ** po) == 1이 될때까지 올림
        # 그 이후부터는 po값 1씩 빼기
        # po값이 0 이하면 종료
        while po >= 1:
            if len_x // (2 ** po) <= 1:
                if len_x // (2 ** po) == 1:
                    change_s += (10 ** po)
                    len_x %= (2 ** po)
                po -= 1
            else:
                po += 1
        
        s = str(change_s)

    return answer