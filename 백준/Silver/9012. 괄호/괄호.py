import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
	s = list(input().strip())
	stack = []

	for c in s:
		if c == '(':
			stack.append(c)
		else:
			if not stack or stack[-1] != '(':
				print('NO')
				break
			stack.pop()
	else:
		print('YES' if not stack else 'NO')