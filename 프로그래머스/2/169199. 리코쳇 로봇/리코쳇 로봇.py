from collections import deque

def solution(board):
    H, W = len(board), len(board[0])
    grid = [list(row) for row in board]
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 'R':
                start = (i, j)
            elif grid[i][j] == 'G':
                goal = (i, j)
    q = deque()
    q.append((start[0], start[1], 0))
    visited = [[False]*W for _ in range(H)]
    visited[start[0]][start[1]] = True
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    while q:
        r, c, moves = q.popleft()
        for dr, dc in directions:
            nr, nc = r, c
            while True:
                tr, tc = nr + dr, nc + dc
                if not (0 <= tr < H and 0 <= tc < W): break
                if grid[tr][tc] == 'D': break
                nr, nc = tr, tc
            if nr == r and nc == c: continue
            if (nr, nc) == goal: return moves + 1
            if not visited[nr][nc]:
                visited[nr][nc] = True
                q.append((nr, nc, moves + 1))
    return -1
