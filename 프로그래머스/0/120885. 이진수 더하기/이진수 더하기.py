def solution(bin1, bin2):
    answer = changeBin(changeInt(bin1) + changeInt(bin2))
    return answer

def changeInt(bin1):
    num = 0
    cnt = 1
    
    for i in range(len(bin1)-1, -1, -1):
        num += (cnt * int(bin1[i]))
        cnt *= 2
        
    return num

def changeBin(int1):
    num = ""
    cnt = 1
    
    while True:
        if int1 // cnt == 1 or int1 == 0:
            break
        cnt *= 2
        
    
    while True:
        if cnt < 1:
            break
        
        num += str(int1 // cnt)
        int1 %= cnt
        cnt //= 2
    
    return num