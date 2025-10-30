def solution(park, routes):
    h, w = len(park), len(park[0])
    for i in range(h):
        for j in range(w):
            if park[i][j] == 'S':
                x, y = i, j
    dir = {'E': (0, 1), 'W': (0, -1), 'S': (1, 0), 'N': (-1, 0)}
    for route in routes:
        op, n = route.split()
        dx, dy = dir[op]
        nx, ny = x, y
        flag = True
        for _ in range(int(n)):
            nx += dx
            ny += dy
            if not (0 <= nx < h and 0 <= ny < w) or park[nx][ny] == 'X':
                flag = False
                break
        if flag:
            x, y = nx, ny
    return [x, y]
