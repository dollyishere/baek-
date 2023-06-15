import sys
from collections import deque

# 테스트 케이스 개수 T 입력받음
t = int(sys.stdin.readline())

# # 테스트 케이스 담아줄 test_case_list를 deque로 만들어줌
# test_case_list = deque()

# t 만큼 반복하면서, 입력 받아줌
for _ in range(t):
    # 한 테스트 케이스 당 3줄을 입력받음
    test_case_line = []
    for _ in range(3):
        test_case_line.append(sys.stdin.readline().rstrip('\n'))
    # 이때, 배열 길이인 test_case_line[1](2번째 입력 값)은 int화 해줌
    test_case_line[1] = int(test_case_line[1])
    # 이제 문자열로 입력받은 배열의 상태를 숫자가 들어있는 리스트로 전환시킬 것임
    # 만약 배열 길이가 0이라면, 배열 값은 빈 리스트([])로 지정해줌
    if test_case_line[1] == 0:
        test_case_line[2] = []
    # 만약 배열 길이가 1 이상이라면, pop으로 빼낸 후 num_list 변수에 저장
    # 이제 좌우의 [] 제거해주고(strip), split으로 , 제거해준 후, map으로 각 요소를 int화 시킨 후 deque에 저장하여 test_case_line에 다시 넣어줌
    else:
        num_list = test_case_line.pop()
        test_case_line.append(deque(map(int, num_list.lstrip('[').rstrip(']').split(','))))
    
    # 뒤집힘 여부 판단할 변수 reverse_now 생성
    reverse_now = False

    # 이제 테스트 실행
    for test_case_num in range(len(test_case_line[0])):
        # 만약 이번 함수가 R이라면, reverse로 반전시켜줌
        # 데이터양이 많기 때문에, 실제로 뒤집는 함수는 해당될 경우에만 지정함
        # 대신 reverse_now의 값을 반전시키는 것으로 해결
        if test_case_line[0][test_case_num] == 'R':
            if reverse_now:
                reverse_now = False
            else:
                reverse_now = True
        # 만약 명령어가 C라면, 다음과 같이 분류
        else:
            # 만약에 배열이 비어있지 않다면, 첫번째 수를 popleft(반전 x) 또는 pop(반전 o)으로 버려줌
            if test_case_line[2]:
                if reverse_now:
                    test_case_line[2].pop()
                else:
                    test_case_line[2].popleft()
            # 만약 배열이 비어있다면, error 출력한 후 break로 모든 수식을 종료함
            else:
                print('error')
                break
        # 만약, 마지막 함수까지 오류 없이 끝마쳤다면, 현재 배열 상태를 출력해줌
        # 이때 반전된 상태면 reverse를 통해 진짜 반전 시켜줌
        # 그냥 리스트로 변환해서 출력하면 공백도 함께 출력되므로, 내부 상태를 int로 바꾼 후 join으로 묶어 출력
        if test_case_num == len(test_case_line[0]) - 1:
            if reverse_now:
                test_case_line[2].reverse()
            print('['+','.join(map(str, test_case_line[2]))+ ']')