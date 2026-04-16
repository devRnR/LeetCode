import sys

input = sys.stdin.readline

n = int(input())
height = [0] * 1001

min_x = 1000
max_x = 0
max_h = 0
max_pos = 0

for _ in range(n):
	x, h = map(int, input().split())
	height[x] = h
	min_x = min(min_x, x)
	max_x = max(max_x, x)
	if h > max_h:
		max_h = h
		max_pos = x

area = 0

cur = 0
for x in range(min_x, max_pos + 1):
	cur = max(cur, height[x])
	area += cur

cur = 0
for x in range(max_x, max_pos, -1):
	cur = max(cur, height[x])
	area += cur

print(area)
