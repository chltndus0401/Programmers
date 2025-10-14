import math

def solution(r1, r2):
    answer = 0
    for x in range(1, r2 + 1):
        y2 = int((r2**2 - x**2)**0.5)
        y1 = math.ceil((r1**2 - x**2)**0.5) if x < r1 else 0
        answer += y2 - y1 + 1
    return answer * 4
