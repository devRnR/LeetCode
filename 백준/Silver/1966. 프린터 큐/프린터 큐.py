from collections import deque
import sys

my_input = sys.stdin.readline

T = int(my_input())

for _ in range(T):
	n,m = map(int, my_input().split())
	arr = list(map(int, my_input().split()))

	priority = deque(sorted(arr, reverse=True))
	wq = deque([(i, w) for i, w in enumerate(arr)])
	cnt = 0

	while wq:
		if wq[0][1] == priority[0]:
			priority.popleft()
			w = wq.popleft()
			cnt += 1

			if w[0] == m:
				print(cnt)
				break

		else:
			wq.append(wq.popleft())