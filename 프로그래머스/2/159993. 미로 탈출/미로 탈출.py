from collections import deque

def bfs(start, target, maps):
    n, m = len(maps), len(maps[0])
    visited = [[False]*m for _ in range(n)]
    q = deque()
    q.append((start[0], start[1], 0))
    visited[start[0]][start[1]] = True
    
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    
    while q:
        x, y, dist = q.popleft()
        
        if (x, y) == target:
            return dist
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and maps[nx][ny] != 'X':
                    visited[nx][ny] = True
                    q.append((nx, ny, dist + 1))
    return -1


def solution(maps):
    n, m = len(maps), len(maps[0])
    
    # S, L, E 위치 찾기
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S': S = (i, j)
            if maps[i][j] == 'L': L = (i, j)
            if maps[i][j] == 'E': E = (i, j)
    
    # 1) S -> L
    dist1 = bfs(S, L, maps)
    if dist1 == -1:
        return -1
    
    # 2) L -> E
    dist2 = bfs(L, E, maps)
    if dist2 == -1:
        return -1
    
    return dist1 + dist2
