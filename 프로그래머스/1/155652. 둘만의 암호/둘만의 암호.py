def solution(s, skip, index):
    alpha = [c for c in 'abcdefghijklmnopqrstuvwxyz' if c not in skip]
    result = ''
    for ch in s:
        i = (alpha.index(ch) + index) % len(alpha)
        result += alpha[i]
    return result
