# 논리 참고함

def solution(e, starts):
    answer = []
    # 범위 내로 억억단 진행한 기록 담아줄 multi_table
    multi_table = [1] * (e + 1)
    # starts 각 값을 정렬한 sort_s, 나중에 값 담을 check dict, 최대 인덱스 기록할 memo 생성
    sort_s = sorted(starts)
    check = dict()
    memo = 0
    
    # 약수로 계산하기
    # 억억단 진행하는 범위만큼 for문 돌리기
    for i in range(2, e+1):
        # i부터 e+1 사이의 범위를 i 만큼 건너 뛰면서 진행하면 억억단!
        # 해당하는 값을 인덱스로 하여 +1 해주기
        for j in range(i, e+1, i):
            multi_table[j] += 1
    
    # sort_s에 담긴 s들 가져오기
    # 해당 문제는 범위 별로 s~e 사이에 많이 나온 값을 확인하는 것임
    # 즉, 먼저 s를 가장 작은 수부터 시작해서 max 값을 구하고, check에 key(s값)-value(많이 나온 인덱스) 형태로 저장해둔 뒤 이 값을 memo에 저장해둠
    # 이후 s부터는 memo 값과 대조함
    # 만약 memo가 s보다 크거나 같다면, 이미 이 아이는 해당 범위 내에서 가장 많이 나온 값이라는 것이 증명됐으므로 추가 검증할 필요 없음
    # 더 작다면, 재검증함
    for s in sort_s:
        if memo == 0:
            max_i = multi_table[s:].index(max(multi_table[s:]))+s
            check[s] = max_i
            memo = max_i
        else:
            if s > memo:
                max_i = multi_table[s:].index(max(multi_table[s:]))+s
                check[s] = max_i
                memo = max_i
            else:
                check[s] = memo
    
    # 모든 가장 많이 등장한 수 구한 뒤, starts 길이만큼 for문 진행
    # 이제 순서대로 start 정답 check에서 뽑아내어 answer에 추가
    for start in starts:
        answer.append(check.get(start))
        
    # 시간초과
    
    # for s in starts:
    #     cnt_dict = dict()
    #     for n in range(s, e+1):
    #         if multi_table[n] not in cnt_dict:
    #             cnt_dict[multi_table[n]] = [n]
    #         else:
    #             cnt_dict[multi_table[n]].append(n)
    #     max_cnt = max(cnt_dict.items())
    #     answer.append(max_cnt[1][0])
    
    return answer