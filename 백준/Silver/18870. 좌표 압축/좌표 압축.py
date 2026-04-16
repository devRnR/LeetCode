import sys
input = sys.stdin.readline

n = int(input())
x_arr = list(map(int, input().split()))
x_sorted = sorted(x_arr)

l = [x_sorted[0]]
answer = [0]
memo = { x_sorted[0]: 0,}

for x in x_sorted[1:]:
	if l[-1] == x:
		answer.append(answer[-1])
	else:
		answer.append(answer[-1]+1)
		l.append(x)
	memo[x] = answer[-1]

for x in x_arr:
	print(memo[x], end=' ')
