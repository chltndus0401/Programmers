from itertools import combinations

def solution(n, q, ans):
    cnt = 0
    
    for code in combinations(range(1, n+1), 5):
        valid = True
        for qi, a in zip(q, ans):
            # code와 qi의 교집합 크기 계산
            if len(set(code) & set(qi)) != a:
                valid = False
                break
        if valid:
            cnt += 1
            
    return cnt
