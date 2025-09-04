from collections import deque

import sys

my_input = sys.stdin.readline

n, k = map(int, my_input().split())
q = deque(range(1, n+1))
memo = []

while len(q) > 1:
	for _ in range(k - 1):
		q.append(q.popleft())
	memo.append(q.popleft())

memo.append(q.popleft())
print("<",", ".join(map(str, memo)), ">", sep='')
