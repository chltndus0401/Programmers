from itertools import combinations
from collections import Counter

def solution(orders, course):
    res=[]
    for c in course:
        cnt=Counter()
        for o in orders:
            if len(o)>=c:
                s=''.join(sorted(o))
                cnt.update([''.join(comb) for comb in combinations(s,c)])
        if not cnt:
            continue
        m=max(cnt.values())
        if m>=2:
            res+=[k for k,v in cnt.items() if v==m]
    return sorted(res)
