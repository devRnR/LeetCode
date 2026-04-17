from math import ceil

def solution(n, left, right):
    return [ max(ceil( i / n), (i-1) % n + 1) for i in range(left + 1, right + 2)]
