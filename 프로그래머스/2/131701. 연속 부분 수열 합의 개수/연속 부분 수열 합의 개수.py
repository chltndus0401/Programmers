def solution(elements):
    n = len(elements)
    arr = elements * 2
    prefix = [0]
    
    for x in arr:
        prefix.append(prefix[-1] + x)
    
    sums = set()
    
    for length in range(1, n + 1):
        for start in range(n):
            end = start + length
            sums.add(prefix[end] - prefix[start])
    
    return len(sums)
