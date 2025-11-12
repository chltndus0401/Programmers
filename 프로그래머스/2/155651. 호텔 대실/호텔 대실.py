import heapq

def solution(book_time):
    def to_min(t):
        h, m = map(int, t.split(':'))
        return h * 60 + m
    books = [(to_min(s), to_min(e) + 10) for s, e in book_time]
    books.sort()
    heap = []
    for s, e in books:
        if heap and heap[0] <= s:
            heapq.heappop(heap)
        heapq.heappush(heap, e)
    return len(heap)
