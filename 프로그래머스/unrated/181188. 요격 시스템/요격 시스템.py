def solution(targets):
    answer = 0
    # e를 기준으로 정렬
    targets.sort(key=lambda x : x[1])
    # 처음 미사일 위치 범위 바깥에서 생성
    misile = -1
    
    for target in targets:
        # 개구간으로 표현되는 폭격 미사일은 s나 e에서 발사할 수 없음
        # 따라서 만약 요격 미사일 위치가 s와 같아도, 추가 설치가 필요
        if misile <= target[0]:
            misile = target[1]
            answer += 1
            
    return answer