# 미생물 이동 함수를 생성
def move():
    # 미생물 이동 후 위치를 파악할 2차원 배열 change와 각 미생물 군체의 정보를 담아줄 리스트 hive 생성
    change = [[[] for _ in range(N)] for _ in range(N)]
    hive = list()

    # 현 미생물 군체들의 정보가 담긴 micro 내부의 미생물 군체 정보(m)를 각각 for문을 통해 확인함
    for m in micro:
        # 이 시점에서 m 안에는 세로 위치(인덱스 0), 가로 위치(1), 미생물 수(2), 이동 방향(3) 총 4 요소가 들어있다.
        # 이동 위치를 따라 이동할 필요가 있으므로, 4중 if문(상하좌우)을 통해 이동방향이 어디인지를 확인한 후 이동 후 좌표값 i, j를 배정한다. 
        if m[3] == 1:
            i, j = m[0] - 1, m[1]
        elif m[3] == 2:
            i, j = m[0] + 1, m[1]
        elif m[3] == 3:
            i, j = m[0], m[1] - 1
        elif m[3] == 4:
            i, j = m[0], m[1] + 1


        # change에서 해당 좌표에 m[2], m[3](각각 미생물 수, 이동방향) 값을 넣은 리스트를 append로 추가해준다.
        change[i][j].append([m[2], m[3]])

    # 모든 미생물의 이동이 끝났다면 이제 미생물의 병합과 새로운 미생물 군체들의 정보를 수집하고 정리할 차례다.
    # 2중 for문을 사용해 change의 각 좌표를 확인해준다.
    for x in range(N):
        for y in range(N):

            # 이 시점에서 change의 각 좌표에는 3가지 가능성이 있다.
            # 미생물이 하나이거나, 2개 이상(다수)이거나, 아예 존재하지 않는 것이 그것이다.
            # 만약 미생물이 없을 경우나 하나일 경우에는 그냥 패스해도 되지만, 만약 2개 이상이면 합쳐져야 한다.
            if len(change[x][y]) >= 1:

                # 만약 미생물 수가 2개 이상일 시, 병합을 진행한다.
                # 방향 전환 기준을 검증할 변수 big과 미생물 총 수를 담을 total, 방향을 담을 way를 생성한 후 초기값을 모두 0으로 맞춰준다.
                # 그 다음으로는 for문을 통해 해당 좌표 내에 있는 각 리스트들을 검증한다.
                # total에는 미생물의 수를 더해주며, 만약 그 수가 현재 big의 크기보다 크다면 way의 값을 해당 리스트 내부의 이동 방향 값으로 바꿔준다.
                # 모든 절차가 끝나면, hive에 좌표값, 총 미생물 수, 방향을 넣어 추가해준다.

                if len(change[x][y]) >= 2:
                    big, total, way = 0, 0, 0
                    for c in change[x][y]:
                        total += c[0]
                        if c[0] > big:
                            big = c[0]
                            way = c[1]
                    hive.append([x, y, total, way])

                # 이제 해당 미생물 군집이 약품이 칠해진 셀 내부에 있는지를 검중한다.
                # 군집들이 있는 장소는 정사각형, 즉 4변에 약품이 칠해져 있는 상황이니 가능성도 4가지가 있다.
                # 만약 해당 범위 내에 있다면, 미생물 수를 반으로 줄여준 후, 방향도 그에 맞게 지정해준 후 hive에 해당 군체 정보를 저장하면 된다. 
                
                elif x == 0:
                    hive.append([x, y, change[x][y][0][0] // 2, 2])
                elif x == N - 1:
                    hive.append([x, y, change[x][y][0][0] // 2, 1])
                elif y == 0:
                    hive.append([x, y, change[x][y][0][0] // 2, 4])
                elif y == N - 1:
                    hive.append([x, y, change[x][y][0][0] // 2, 3])

                # 그 어디에도 해당되지 않는 군체는, 그냥 그대로 다음 루프를 돌 수 있도록 갱신된 정보 그대로 hive에 저장하면 된다.
                else:
                    hive.append([x, y, change[x][y][0][0], change[x][y][0][1]])
    
    # 모든 절차가 끝난 후, hive를 리턴한다.
    return hive

# 총 테스트 케이스 수를 입력받는다.
T = int(input())

# 테스트 케이스 총 수만큼 반복한다.
for tc in range(1, T+1):

    # N(셀의 개수), M(격리시간), K(미생물 군집 개수)를 각각 map을 통해 정수화하여 입력 받는다.
    N, M, K = map(int, input().split())
    # 각 미생물 군체의 정보(세로, 가로 위치, 미생물의 수, 이동방향)를 2중 리스트 형태로 받아준다.
    micro = [list(map(int, input().split())) for _ in range(K)]

    # 본 문제의 정답을 담아줄 변수 answer를 생성한다(초기값 0)
    answer = 0

    # M 시간 동안 미생물 군체의 이동이 반복된다.
    # for문으로 M번만큼 반복하면서, micro 리스트를 move()함수를 통해 구한 hive 리스트로 변경해준다.
    for m in range(M):
        micro = move()
    
    # M번만큼 이동이 끝난 후, micro 리스트 내부의 각 리스트들을 조회하면서 m[2](미생물의 수) 값을 answer에 저장해준다.
    for m in micro:
        answer += m[2]

    # 모든 연산이 끝난 후, 테스트 케이스 번호와 정답을 출력해준다.
    print('#{} {}'.format(tc, answer))