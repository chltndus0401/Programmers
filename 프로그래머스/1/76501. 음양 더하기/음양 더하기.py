def solution(absolutes, signs):
    total = 0
    for num, sign in zip(absolutes, signs):
        total += num if sign else -num
    return total

