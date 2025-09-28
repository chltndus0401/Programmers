def solution(wallet, bill):
    wallet = sorted(wallet)
    def fold_count(bill):
        bill = sorted(bill)
        count = 0
        while not (bill[0] <= wallet[0] and bill[1] <= wallet[1]):
            if bill[0] >= bill[1]:
                bill[0] //= 2
            else:
                bill[1] //= 2
            bill.sort()
            count += 1
        return count
    return min(fold_count(bill), fold_count(bill[::-1]))
