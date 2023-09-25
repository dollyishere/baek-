import sys

n, k = map(int, sys.stdin.readline().split())
coins = []
# dp에 저장하는 것은 코인 수임
# 정확히는, 현 인덱스 값을 만드는 데에 필요한 최소 코인 수를 담는 리스트가 됨
dp = [10000001] * (k + 1)

for _ in range(n):
    coins.append(int(sys.stdin.readline().rstrip()))

# dp[0]은 당연히 0이므로 0으로 배정
dp[0] = 0

# 현재 보유한 코인 하나씩 꺼내보기
for coin in coins:
    # 현재 코인 값과 k까지 반복
    # dp[i]의 값은 coin와 k 사이의 값인 i를 만드는 데 사용된 값일 것
    # 반대로 dp[i-coin]값은 i-coin 값을 만드는 데 사용된 최소 코인 값임
    # 즉 현재 값을 만드는 dp[i] 값(디폴트 10000001)과 dp[i-coin]+1 중 어느 쪽이 더 가벼운 값인지 확인
    # 더 적은 값을 배정해줌

    # 정확히는 현재 코인 값도 파악해서 비교하는 듯?
    # dp[i-coin]+1과 비교하는 이유는 어차피 현재 값보다 작으므로, 거기에 1만 더해도 현재 i 값을 산출해낼 수 있는지?의 문제인듯
    for i in range(coin, k+1):
        # print(dp)
        # print(i, dp[i], dp[i-coin], dp[i-coin]+1)
        dp[i] = min(dp[i], dp[i-coin]+1)

# 만약 dp[k]이 10000001라면, 해당 값은 만들 수 없는 값임
# -1 출력
if dp[k] == 10000001:
    print(-1)
# 아니라면 dp[k] 출력
else:
    print(dp[k])


