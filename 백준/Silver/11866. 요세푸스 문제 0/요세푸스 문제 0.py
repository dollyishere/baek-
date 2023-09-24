n, k = map(int, input().split())

circle = []
answer = "<"

cnt = 0

for i in range(1, n+1):
    circle.append(i)


while circle:
    cnt += (k-1)
    cnt %= n
    answer += str(circle.pop(cnt))
    n -= 1
    if n != 0:
        answer += ", "
        
print(answer + ">") 