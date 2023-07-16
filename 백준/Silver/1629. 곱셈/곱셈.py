# 분할 정복 문제
a, b, c = map(int, input().split())

# 약간 재귀식으로 가야 하는 듯?
# 만약 b가 1일 경우, 그냥 a % c 나머지 값을 넘겨주면 됨(수식 종료 포인트)
def dac(a, b, c):
    if b == 1:
        return a % c
    # 만약 b가 2의 배수라면, b를 2로 나눈 값을 분할정복으로 수행하고 c를 나머지로 한 값 리턴
    elif b % 2 == 0:
        return (dac(a, b//2, c) ** 2) % c
    # 2의 배수가 아닐 시, a를 한번 더 곱해주는 걸로 한 번 더 계산해준 후 c로 나눈 값 출력
    else:
        return ((dac(a, b//2, c) ** 2) * a) % c

print(dac(a, b, c))