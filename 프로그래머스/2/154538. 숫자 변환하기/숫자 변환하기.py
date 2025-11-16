from collections import deque

def solution(x, y, n):
    q = deque()
    q.append((x, 0)) 
    visited = set([x])
    
    while q:
        v, cnt = q.popleft()
        
        if v == y:
            return cnt
        
       
        for nv in (v + n, v * 2, v * 3):
            if nv <= y and nv not in visited:
                visited.add(nv)
                q.append((nv, cnt + 1))
    
    return -1
