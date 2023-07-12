# dp문제(어렵당...) 

# 페인트할 집의 수와 각 집마다 정해진 페인트 가격 입력받기
n = int(input())
paint_pay = []

# 빨강, 초록, 파랑 순
for _ in range(n):
    paint_pay.append(list(map(int, input().split())))

# 각 집이 페인트 받을 가능성은 색깔마다 있으므로, 3가지라 할 수 있음
# 따라서 인덱스를 3개 가진 리스트를 집의 수만큼 만들어 pain_pay_state 변수에 저장해줌
paint_pay_state = [[1001] * 3 for _ in range(n)]
# 이중 첫 집은 나중에 칠하는 집의 영향을 받지 않으므로 이미 정해진 가격(paint_pay[0])을 배정
paint_pay_state[0] = paint_pay[0]

# 첫 집을 제외한 나머지 집들의 가격을 dp로 계산
for i in range(1, n):
    # 페인트 색만큼의 가능성을 분석
    # 앞, 뒤 집과 페인트 색이 겹치면 안된다는 조건이 있었음
    # but 현 상황에서는 어차피 뒷집에서 검증할 때 앞집의 색과 겹치지 않기 위해 신경쓸 것이므로 뒷집의 페인트 색은 신경쓰지 않아도 됨
    # 따라서 앞집과 다른 페인트 색을 칠할 경우(2가지)만 생각하여 해당 인덱스에 담긴 값 중 최소값을 선택한 후, 이번에 선택한 페인트 값을 더해 인덱스에 넣어줌
    paint_pay_state[i][0] = min(paint_pay_state[i-1][1], paint_pay_state[i-1][2]) + paint_pay[i][0]
    paint_pay_state[i][1] = min(paint_pay_state[i-1][0], paint_pay_state[i-1][2]) + paint_pay[i][1]
    paint_pay_state[i][2] = min(paint_pay_state[i-1][0], paint_pay_state[i-1][1]) + paint_pay[i][2]

# 그렇게 되면 마지막으로 페인트를 칠한 집의 리스트 안에는 해당 색들을 칠하기까지의 페인트 값의 합산이 담겨 있을 것임
# 그 중에서 최소값을 min으로 찾아내어 출력함(정답)
print(min(paint_pay_state[n-1]))