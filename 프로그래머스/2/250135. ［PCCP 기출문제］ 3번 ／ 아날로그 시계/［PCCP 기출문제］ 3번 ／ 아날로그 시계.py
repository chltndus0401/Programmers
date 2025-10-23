from fractions import Fraction

def solution(h1, m1, s1, h2, m2, s2):
    start = h1 * 3600 + m1 * 60 + s1
    end = h2 * 3600 + m2 * 60 + s2
    times = set()
    nmin = (start * 59 + 3600 - 1) // 3600
    nmax = (end * 59) // 3600
    for n in range(nmin, nmax + 1):
        t = Fraction(3600 * n, 59)
        if start <= t <= end:
            times.add(t)
    mmin = (start * 719 + 43200 - 1) // 43200
    mmax = (end * 719) // 43200
    for m in range(mmin, mmax + 1):
        t = Fraction(43200 * m, 719)
        if start <= t <= end:
            times.add(t)
    return len(times)
