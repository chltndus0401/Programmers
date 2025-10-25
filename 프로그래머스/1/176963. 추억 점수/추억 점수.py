def solution(name, yearning, photo):
    score = {n: y for n, y in zip(name, yearning)}
    return [sum(score.get(p, 0) for p in people) for people in photo]
