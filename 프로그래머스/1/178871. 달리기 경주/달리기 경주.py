def solution(players, callings):
    rank = {player: i for i, player in enumerate(players)}
    for c in callings:
        i = rank[c]
        players[i], players[i - 1] = players[i - 1], players[i]
        rank[players[i]] = i
        rank[players[i - 1]] = i - 1
    return players
