def solution(sequence, k):
    n = len(sequence)
    left, right = 0, 0
    total = sequence[0]
    answer = [0, n - 1]

    while left < n and right < n:
        if total == k:
            if (right - left) < (answer[1] - answer[0]):
                answer = [left, right]
            left += 1
            if left < n:
                total -= sequence[left - 1]
        elif total < k:
            right += 1
            if right < n:
                total += sequence[right]
        else:
            total -= sequence[left]
            left += 1

    return answer
