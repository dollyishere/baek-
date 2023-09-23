def solution(plans):
    answer = []
    new_plans = []
    staging_plans = []
    now_time = 0
    
    def time_change(str_time):
        hour = int(str_time[:2])
        minute = int(str_time[3:])
        return hour * 60 + minute
    
    for plan in plans:
        new_plans.append([plan[0], time_change(plan[1]), int(plan[2])])
    
    new_plans.sort(key=lambda x : x[1])
    
    for i in range(len(plans)-1):
        now_plan = new_plans[i]
        next_plan = new_plans[i+1]
        ex_time = now_plan[1]+now_plan[2]
        if ex_time == next_plan[1]:
            now_time = next_plan[1]
            answer.append(now_plan[0])
        elif ex_time > next_plan[1]:
            staging_plans.append(now_plan[:2]+[ex_time-next_plan[1]])
        else:
            answer.append(now_plan[0])
            now_time = ex_time
            while staging_plans != []:
                now_plan = staging_plans.pop()
                ex_time = now_time+now_plan[2]
                if ex_time == next_plan[1]:
                    now_time = next_plan[1]
                    answer.append(now_plan[0])
                    break
                elif ex_time > next_plan[1]:
                    staging_plans.append(now_plan[:2]+[ex_time-next_plan[1]])
                    break
                else:
                    now_time = ex_time
                    answer.append(now_plan[0])
    
    answer.append(new_plans[-1][0])
    if staging_plans != []:
        for i in range(len(staging_plans)-1, -1, -1):
            answer.append(staging_plans[i][0])
    
    return answer