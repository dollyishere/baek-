# 연산을 원하는 수 n 입력받음
n = int(input())

# 다이나믹 프로그래밍(dp)을 기록(메모이제이션)할 배열 dp 생성
# 이때 n의 연산과 같게 하기 위해 n+1 길이만큼 만들어줌
dp = [0] * (n + 1)

# bottom-up으로, 아래 숫자부터 연산
# 0과 1은 연산할 필요가 없으므로, 2부터 시작
now_num = 2

# now_num이 n과 같아질 때까지 while문으로 반복
while now_num <= n:
    # 연산 3번(1을 뺀다)를 먼저 수행해줌
    # now_num에서 -1을 뺀 dp 인덱스의 값에 1을 더해(연산을 한 번 더 했다는 뜻) 현재 now_num을 인덱스로 가진 dp에 넣어줌
    dp[now_num] = dp[now_num-1] + 1
    
    # 이제 2번 연산이 가능한지 검사함
    # 만약 now_num이 2로 나누어지고, now_num을 2로 나눈 값의 dp 인덱스 내부값에 1을 더한 값이 현재 now_num 인덱스에 담긴 값보다 작다면,
    # 해당 값을 dp[now_num]에 넣어줌
    if now_num % 2 == 0 and dp[now_num // 2] + 1 < dp[now_num]:
        dp[now_num] = dp[now_num//2] + 1
    
    # 다음에는 3번 연산이 가능한지 검사함
    # 만약 now_num이 3으로 나누어지고, now_num을 3으로 나눈 값의 dp 인덱스 내부값에 1을 더한 값이 현재 now_num 인덱스에 담긴 값보다 작다면,
    # 해당 값을 dp[now_num에 넣어줌]
    if now_num % 3 == 0 and dp[now_num // 3] + 1 < dp[now_num]:
        dp[now_num] = dp[now_num//3] + 1

    # now_num에 1을 더해 다음 값을 검증할 수 있도록 함
    now_num += 1

# 현재 dp[n]에 담긴 값을 출력(정답)
print(dp[n])
    