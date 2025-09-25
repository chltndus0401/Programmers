def solution(schedules, timelogs, startday):
    successful_employees = 0
    num_employees = len(schedules)

    for i in range(num_employees):
        schedule_time = schedules[i]
        schedule_hour = schedule_time // 100
        schedule_minute = schedule_time % 100
        
        deadline_in_minutes = (schedule_hour * 60 + schedule_minute) + 10

        was_never_late = True
        
        for j in range(7):
            day_of_week = ((startday - 1) + j) % 7

            if day_of_week >= 5:
                continue

            arrival_time = timelogs[i][j]
            arrival_hour = arrival_time // 100
            arrival_minute = arrival_time % 100
            
            arrival_in_minutes = arrival_hour * 60 + arrival_minute

            if arrival_in_minutes > deadline_in_minutes:
                was_never_late = False
                break
        
        if was_never_late:
            successful_employees += 1
            
    return successful_employees