def solution(players, m, k):
    expire = [0] * (24 + k + 1)
    active = 0
    total = 0
    for i in range(24):
        active -= expire[i]
        need = players[i] // m
        if active < need:
            delta = need - active
            total += delta
            active += delta
            expire[i + k] += delta
    return total
