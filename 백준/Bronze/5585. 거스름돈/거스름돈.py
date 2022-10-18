pay = int(input())
money = 1000 - pay
answer = 0

while True:
    if money == 0:
        break
    else:
        if money >= 500:
            money -= 500
        elif money >= 100:
            money -= 100
        elif money >= 50:
            money -= 50
        elif money >= 10:
            money -= 10
        elif money >= 5:
            money -= 5
        elif money >= 1:
            money -= 1
        answer += 1

print(answer)