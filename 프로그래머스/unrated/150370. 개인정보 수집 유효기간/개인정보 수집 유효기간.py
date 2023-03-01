def solution(today, terms, privacies):
    answer = []
    check = 1
    for privacy in privacies:
        year = int(privacy[:4])
        month = int(privacy[5:7])
        day = int(privacy[8:10])
        rule = privacy[-1]
        
        for term in terms:
            if rule in term:
                year += (int(term[2:]) // 12) 
                month += (int(term[2:]) % 12) 
                if month > 12:
                    year += 1
                    month -= 12
                break

                
        if (year > int(today[:4])) :      
            pass
        elif (year == int(today[:4])):
            if (month > int(today[5:7])):             
                pass
            elif (month  == int(today[5:7])):
                if (day > int(today[8:])):
                    pass
                else:
                    answer.append(check)
            else:
                answer.append(check)
        else:
            answer.append(check)
        check += 1
            
    return answer