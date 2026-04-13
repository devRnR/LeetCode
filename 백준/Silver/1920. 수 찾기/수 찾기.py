import sys

input = sys.stdin.readline
n = int(input())
n_arr = { k: 1 for k in map(int, input().split()) }

m = int(input())
m_arr = list(map(int, input().split()))

for num in m_arr:
    print(1 if num in n_arr else 0)
