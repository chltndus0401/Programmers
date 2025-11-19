def solution(a, b, n):
    ans = 0
    while n >= a:
        q = (n // a) * b
        ans += q
        n = n % a + q
    return ans
