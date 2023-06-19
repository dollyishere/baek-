# n, m, s 입력받음
n = int(input())
m = int(input())
s = input()

# 정답으로 출력할 answer 변수 생성
answer = 0
# 현재 Pn이 어떤 상태인지 미리 만들어둠
now_p = 'I' + 'OI' * n

# out of range 안나도록 m-n 범위에서만 반복
for i in range(m-n):
    # 만약 s[i]가 I라면, 검증함
    # check_p로 가능 범위만큼 s를 슬라이싱한 결과를 넣어준 후, 미리 만들어둔 now_p와 대조
    # 만약 일치한다면, answer에 +1 해줌
    if s[i] == 'I':
        check_p = s[i:i+n*2+1]
        if check_p == now_p:
            answer += 1

# 정답 출력함
print(answer)
