import sys
input = sys.stdin.readline

n = int(input())
x_arr = list(map(int, input().split()))
x_sorted = sorted(set(x_arr)) # O(n log n)

memo = { x: i for i, x in enumerate(x_sorted)}

for x in x_arr: # O(n)
	print(memo[x], end=' ')
