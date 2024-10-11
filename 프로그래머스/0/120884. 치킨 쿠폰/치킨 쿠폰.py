def solution(chicken):
    answer = chicken // 10
    ticket = chicken % 10 + chicken // 10
    
    while (True):
        if ticket < 10:
            break
        
        get_ticket = ticket % 10 + ticket // 10
        answer += ticket // 10
        
        ticket = get_ticket
        
    
    return answer