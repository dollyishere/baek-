# DP(냅색 계열?) or 백트래킹?
# 순서만 바꿔줘도 괜찮을 것 같기도 하고...(포기~~~~~~~~~!)
# 이걸 DFS로 어케 품...???????
# 풀이 대단히 참고............... https://hyunse0.tistory.com/330

# 현재까지의 확률 total을 받아주는 f 함수 제작
def f(total):
    # 정답이자 최대 확률 변수 maxv 글로벌 선언해줌
    global maxv

    # 본 문제는 확률을 구하는 문제임
    # 즉, 현재 mavx값보다 작거나 같으면 이제부터 더 작아질 일 밖에 없음(남은 계산식은 다 1 미만 소수를 더해주기 때문임)
    # 따라서 이 시점에서 가지치기해줌
    if total <= maxv:
        return
    # 만약 현 stack(현재까지 확률들 담아준 리스트)의 길이가 N과 같다면, 모든 인원에게 모든 업무가 배정되었다는 뜻임
    # 현재 maxv값과 비교해 더 큰 값을 골라 maxv에 넣고, 이 시점에서 해당 분기는 계산을 종료, return해줌
    elif len(stack) == N:
        maxv = max(maxv, total)
        return
    # 만약 위의 두 가지 탈출 조건에 해당한다면, for문을 이용하여 모든 가능성 조회
    # N 이하의 i 값이 아직 stack내에 존재하지 않다면, 아직 일을 배정받지 못한 일꾼이라는 뜻임
    # stack에 i를 집어넣어준 후(이제 이 인원은 일하러 가게 됨!) 재귀를 진행함
    # 이때 현재 total값을 갱신하여 넣어줌
    # 현재 일을 배정받은 사람의 번호(stack[-1])로 employee 리스트를 조회한 후, 현재 아직 비어 있는 일(len(stack) - 1)을 선택하여 total에 곱한 후, 100으로 나눠줌
    # 재귀를 실행한 후에는 pop을 통해 i를 빼내줌(이후 다른 순서의 배열을 완성시키기 위함)
    else:
        for i in range(N):
            if i not in stack:
                stack.append(i)
                f(total * employee[stack[-1]][len(stack) - 1] / 100)
                stack.pop()

# 총 테스트 케이스 수 받아와줌
T = int(input())

# 테스트 케이스 수만큼 반복
for tc in range(1, T+1):

    # 일꾼의 수이자 일거리의 수인 N를 받아와줌
    N = int(input())
    
    # N줄만큼 현재 일꾼의 각 일거리별 업무 역량(성공률)을 받아와줌
    employee = [list(map(int, input().split())) for _ in range(N)]

    # 정답으로 출력할 최대 성공률을 담아줄 변수 maxv를 지정
    maxv = 0

    # f함수에서 사용할 비어있는 리스트 stack을 생성함
    stack = list()

    # 초기값 1로 하여 f함수 실행
    # 초기 total 값을 1로 지정해주는 이유는 이를 기준으로 소수 값을 곱해줄 예정이기 때문임(아무것도 시도하지 않으면 일단 성공률은 1이다...)
    f(1)

    # 모든 연산 끝난 후, 먼저 maxv에 100을 곱해준 후, format 서식을 통해 소수점 뒷자리를 6번째까지 출력해줌
    print('#{} {:.6f}'.format(tc, maxv * 100))