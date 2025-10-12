def solution(targets):
    targets.sort(key=lambda x: x[1])
    count = 0
    last = -1

    for s, e in targets:
        if s >= last:
            count += 1
            last = e
    return count
