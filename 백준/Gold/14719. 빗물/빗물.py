import sys

input = sys.stdin.readline

h,w = map(int, input().split())
height = list(map(int, input().split()))

min_x = 0
max_x = w - 1
max_h = 0
max_pos = 0

for i, h in enumerate(height):
	if h > max_h:
		max_h = h
		max_pos = i

area = 0

cur = 0
for i in range(min_x, max_pos + 1):
	cur = max(cur, height[i])
	area += cur - height[i]


cur = 0
for i in range(max_x, max_pos, -1):
	cur = max(cur, height[i])
	area += cur - height[i]

print(area)