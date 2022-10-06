num = input()

original = num
cnt = 0

while True:
    cnt += 1
    if int(num) < 10:
        gogo = num
        num += '0'
    else:
        gogo = num[1]
    
    total = int(num[0]) + int(num[1])
    num = gogo + str(total)[-1]
    if int(num) == int(original):
        break
    num = str(int(num))

print(cnt)