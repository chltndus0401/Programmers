def solution(t, p):
    lp = len(p)
    pv = int(p)
    c = 0
    for i in range(len(t) - lp + 1):
        if int(t[i:i+lp]) <= pv:
            c += 1
    return c
