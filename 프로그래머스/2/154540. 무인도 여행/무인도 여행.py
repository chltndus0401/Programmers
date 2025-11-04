from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[False]*m for _ in range(n)]
    result = []
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visited[i][j]:
                q = deque([(i, j)])
                visited[i][j] = True
                total = int(maps[i][j])
                while q:
                    x, y = q.popleft()
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] != 'X':
                            visited[nx][ny] = True
                            total += int(maps[nx][ny])
                            q.append((nx, ny))
                result.append(total)
    
    return sorted(result) if result else [-1]
