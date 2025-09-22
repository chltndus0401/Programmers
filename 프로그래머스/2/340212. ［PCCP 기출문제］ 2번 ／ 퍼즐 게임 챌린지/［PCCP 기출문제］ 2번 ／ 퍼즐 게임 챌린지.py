def solution(diffs, times, limit):
    left = 1
    right = 100001
    min_level = right

    while left <= right:
        level = (left + right) // 2
        total_time = 0

        total_time += times[0]

        for i in range(1, len(diffs)):
            diff = diffs[i]
            time_cur = times[i]
            time_prev = times[i - 1]

            if diff <= level:
                total_time += time_cur
            else:
                mistakes = diff - level
                penalty_per_mistake = time_cur + time_prev
                puzzle_time = mistakes * penalty_per_mistake + time_cur
                total_time += puzzle_time
            
            if total_time > limit:
                break

        if total_time <= limit:
            min_level = level
            right = level - 1
        else:
            left = level + 1
            
    return min_level