from collections import Counter

# Counter의 경우, 리스트 내의 원소들과 그 수를 체크하여 딕셔너리 형태로 만들어주는 함수임
def solution(toppings):
    answer = 0
    mine, bro = set(), Counter(toppings)
    mine_num, bro_num = 0, len(bro)
    
    for topping in toppings:
        bro[topping] -= 1
        # Counter의 경우, 해당 키 값이 0이더라도 그걸 구별하기 힘드므로 따로 num 값을 만들어 개수가 0인 토핑이 발생할 시, bro_num에서 차감하는 것으로 해결
        if bro[topping] == 0:
            bro_num -= 1
        
        # 만약 철수의 롤케이크에 해당 토핑이 없을 시, 토핑 추가
        if topping not in mine:
            mine.add(topping)
            mine_num += 1
        
        # 만약 철수 롤케이크의 토핑 개수가 동생과 같다면, answer에 1을 더해줌 
        if mine_num == bro_num:
            answer += 1
        
        # 만약 철수 롤케이크 토핑 개수가 동생보다 더 크다면, 추가 검증은 필요 없으므로 반복문 탈출
        if mine_num > bro_num:
            break
            
    # 답 리턴
    return answer