import sys

input = sys.stdin.readline

n = int(input())
heights = [int(input()) for i in range(n)]

stack = []
max_area = 0

for i, h in enumerate(heights):
	start = i
	while stack and stack[-1][1] > h:
		idx, prev_h = stack.pop()
		max_area = max(max_area, prev_h * (i - idx))
		start = idx

	stack.append((start, h))

for i, h in stack:
	max_area = max(max_area, h * (n - i))

print(max_area)