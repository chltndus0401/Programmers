def solution(s):
    cnt = 0
    removed = 0
    while s != "1":
        zero = s.count('0')
        removed += zero
        s = bin(len(s) - zero)[2:]
        cnt += 1
    return [cnt, removed]
