from itertools import combinations

def solution(number):
    return sum(1 for a,b,c in combinations(number,3) if a+b+c==0)
