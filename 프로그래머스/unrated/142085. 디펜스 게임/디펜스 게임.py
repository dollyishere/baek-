import heapq

def solution(n, k, enemy):
    answer = 0
    # 무적권 사용했는지 아닌지 여부 확인
    # 사용한 수는 어떻게 구분???
    # 우선순위 큐 문제
    heap = []
    damage = 0
    
    for now_e in enemy:
        heapq.heappush(heap, -now_e)
        damage += now_e
        if damage > n:
            if k:
                damage += heapq.heappop(heap)
                k -= 1
            else:
                break
        answer += 1

    return answer