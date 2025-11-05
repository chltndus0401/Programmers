def solution(keymap, targets):
    d = {}
    for i in keymap:
        for idx, c in enumerate(i):
            if c not in d or d[c] > idx + 1:
                d[c] = idx + 1
    ans = []
    for t in targets:
        s = 0
        for c in t:
            if c not in d:
                s = -1
                break
            s += d[c]
        ans.append(s)
    return ans
