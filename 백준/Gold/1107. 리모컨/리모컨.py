# 보고 싶은 채널 값 n 입력받음
n = int(input())
# 고장난 버튼 수인 m을 입력 받은 후, 0이 아닐 경우에만 broken_buttons을 입력받음
m = int(input())
broken_buttons = []

if m != 0:
    broken_buttons = list(input().split())

# 현재 있는 채널인 100을 기반으로 가기 원하는 채널과의 차이를 절대값으로 구해줌(abs)
push_cnt = abs(100-n)

# 이동하려는 채널은 500000까지지만, 5나 0이 망가졌을 때를 고려하여 1000001로 for문 순회(brute-force)
for i in range(1000001):
    # 현재 i 값을 str로 문자열로 바꿔준 후, now_num에 배정
    now_num = str(i)
    # i의 모든 인덱스 값이 고장난 값인지 아닌지를 판명함
    for part_num in range(len(now_num)):
        # 만약 버튼이 고장났을 시, 해당 채널로 한 번에 이동할 수 없다는 것을 뜻함
        # 우리가 원하는 것은 보고 싶은 채널 값에서 가장 가까운 값까지는 버튼을 눌러 이동한 후, 만약 필요하다면 1씩 증감하는 것임(이게 최단 루트이기 때문)
        # 따라서 버튼이 고장나 갈 수 없는 채널 번호는 검증할 필요가 없기에, break로 탈출해줌
        if now_num[part_num] in broken_buttons:
            break
        # 만약 끝까지 검증했고, 고장난 버튼이 아니라면,
        if part_num == len(now_num) - 1:
            # 현재의 버튼 누른 횟수(push_cnt)와, 현재 채널 번호 값과 원하는 채널 번호 값의 차이(절대값)과 현재 채널 번호의 길이(길이만큼 횟수 증가)를 합한 값을 비교함
            # 그리고 둘 중에 더 작은 값을 min으로 검증하여 push_cnt에 넣어줌
            push_cnt = min(push_cnt, abs(n-i)+len(now_num))

#  모든 연산을 마치고, 최소로 버튼을 눌러 원하는 채널로 이동한 경우를 출력(정답)
print(push_cnt)