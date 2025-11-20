def solution(word):
    w = [781, 156, 31, 6, 1]
    d = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
    ans = 0
    for i, ch in enumerate(word):
        ans += d[ch] * w[i] + 1
    return ans
