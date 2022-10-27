n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
answer = n

for i in range(n):
    a[i] -= b
    if a[i] <= 0:
        pass
    else:
        if a[i] % c == 0:
            answer += (a[i] // c)
        else:  
            answer += (a[i] // c) + 1

print(answer) 
    