import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

stack = []
answer = [-1] * n

for i, n in enumerate(nums):

	while stack and stack[-1][1] < n:
		j, v = stack.pop()
		answer[j] = n
		
	stack.append((i, n))

print(*answer)
