import sys

input = sys.stdin.readline

n = int(input())
n_arr = set(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))

for x in m_arr:
	print(int(x in n_arr), end=' ')