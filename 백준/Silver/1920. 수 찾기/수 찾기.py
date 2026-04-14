import sys
from bisect import *

input = sys.stdin.readline

n = int(input())
n_arr = sorted(map(int, input().split()))

m = int(input())
m_arr = list(map(int, input().split()))

for num in m_arr:
    v = bisect_left(n_arr, num)

    if v < len(n_arr) and n_arr[v] == num:
        print(1)
    else:
        print(0)


