def solution(sizes):
    w = 0
    h = 0
    for a, b in sizes:
        if a < b:
            a, b = b, a
        w = max(w, a)
        h = max(h, b)
    return w * h
