def solution(friends, gifts):
    n = len(friends)
    idx = {name: i for i, name in enumerate(friends)}
    gift_count = [[0] * n for _ in range(n)]
    for g in gifts:
        giver, receiver = g.split()
        gift_count[idx[giver]][idx[receiver]] += 1
    gift_index = [0] * n
    for i in range(n):
        give_total = sum(gift_count[i])
        receive_total = sum(gift_count[j][i] for j in range(n))
        gift_index[i] = give_total - receive_total
    next_receive = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if gift_count[i][j] > gift_count[j][i]:
                next_receive[i] += 1
            elif gift_count[i][j] < gift_count[j][i]:
                next_receive[j] += 1
            else:
                if gift_index[i] > gift_index[j]:
                    next_receive[i] += 1
                elif gift_index[i] < gift_index[j]:
                    next_receive[j] += 1
    return max(next_receive)
