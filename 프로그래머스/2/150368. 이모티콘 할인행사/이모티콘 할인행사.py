from itertools import product

def solution(users, emoticons):
    discounts = [10, 20, 30, 40]
    best_plus = 0
    best_sales = 0

    for rates in product(discounts, repeat=len(emoticons)):
        plus_cnt = 0
        sales = 0
        for user_discount, user_limit in users:
            total = 0
            for emo_price, rate in zip(emoticons, rates):
                if rate >= user_discount:
                    total += emo_price * (100 - rate) // 100
            if total >= user_limit:
                plus_cnt += 1
            else:
                sales += total
        if plus_cnt > best_plus or (plus_cnt == best_plus and sales > best_sales):
            best_plus, best_sales = plus_cnt, sales

    return [best_plus, best_sales]

