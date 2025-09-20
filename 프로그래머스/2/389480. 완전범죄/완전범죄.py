def solution(info, n, m):
    INF = 10**9
    dp = [INF] * m
    dp[0] = 0
    for a, b in info:
        new_dp = [INF] * m
        for j in range(m):
            if dp[j] == INF:
                continue
            na = dp[j] + a
            if na < n:
                if na < new_dp[j]:
                    new_dp[j] = na
            nb = j + b
            if nb < m:
                if dp[j] < new_dp[nb]:
                    new_dp[nb] = dp[j]
        dp = new_dp
    ans = min(dp)
    return ans if ans != INF else -1
