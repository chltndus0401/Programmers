def solution(picks, minerals):
    fatigue = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]
    cnt = sum(picks)
    groups = []
    for i in range(0, len(minerals), 5):
        if cnt == 0: break
        group = minerals[i:i+5]
        groups.append([group.count("diamond"), group.count("iron"), group.count("stone")])
        cnt -= 1
    groups.sort(key=lambda x: (-x[0], -x[1], -x[2]))
    result = 0
    for g in groups:
        if picks[0] > 0:
            pick = 0
            picks[0] -= 1
        elif picks[1] > 0:
            pick = 1
            picks[1] -= 1
        else:
            pick = 2
            picks[2] -= 1
        for i in range(3):
            result += g[i] * fatigue[pick][i]
    return result

