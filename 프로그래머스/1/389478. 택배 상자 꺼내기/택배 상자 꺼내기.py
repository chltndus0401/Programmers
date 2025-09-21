def solution(n, w, num):
    height = (n + w - 1) // w
    warehouse = [[0] * w for _ in range(height)]

    for box_num in range(1, n + 1):
        row = (box_num - 1) // w
        
        if row % 2 == 0:
            col = (box_num - 1) % w
        else:
            col = (w - 1) - ((box_num - 1) % w)
        
        warehouse[row][col] = box_num

    target_row, target_col = -1, -1
    for r in range(height):
        for c in range(w):
            if warehouse[r][c] == num:
                target_row = r
                target_col = c
                break
        if target_row != -1:
            break

    count = 0
    for r in range(target_row, height):
        if warehouse[r][target_col] != 0:
            count += 1
            
    return count