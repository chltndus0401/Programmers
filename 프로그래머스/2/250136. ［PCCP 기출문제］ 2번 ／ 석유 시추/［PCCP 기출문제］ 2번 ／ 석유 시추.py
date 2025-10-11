from collections import deque

def solution(land):
    n, m = len(land), len(land[0])
    visited = [[False]*m for _ in range(n)]
    oil_sizes = [0]*m
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                q = deque([(i,j)])
                visited[i][j] = True
                count = 1
                cols = set([j])

                while q:
                    x, y = q.popleft()
                    for dx, dy in directions:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == 1 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                            count += 1
                            cols.add(ny)

                for c in cols:
                    oil_sizes[c] += count

    return max(oil_sizes)
