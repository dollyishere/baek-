def solution(N, stages):
    # 정답 return 용
    answer = []
    # 현재 stage 상황 기록용
    stage_states = dict()
    # 실패율 기록용
    failed_list = list()
    
    # 모든 스테이지(N+1: 올클 포함) 상황 담을 dict 만들기
    for n in range(1, N+2):
        stage_states[n] = 0
    
    # 현재 스테이지 클리어 상황 기록(이전 스테이지 클리어 기록 포함)
    for stage in stages:
        for s in range(1, stage+1):
            stage_states[s] += 1
    
    # 현 스테이지 실패율 & 현 스테이지 번호(이후 정렬 및 정답 구분 위함) 기록
    for s in range(1, N+1):
        now_challenge = stage_states[s]
        go_next = stage_states[s+1]
        
        if (now_challenge != 0):
            failed_list.append([(now_challenge - go_next) / now_challenge, s])
        else:
            failed_list.append([0, s])
    
    # 실패율은 내림차순, 스테이지 번호는 오름차순으로 정렬
    failed_data_sort = sorted(failed_list, key=lambda x: (-x[0], x[1]))
    
    # 정답 answer 리스트에 담아서 리턴
    for status in failed_data_sort:
        answer.append(status[1])
        
    return answer