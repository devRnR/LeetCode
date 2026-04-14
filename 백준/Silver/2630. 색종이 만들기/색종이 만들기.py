import sys

input = sys.stdin.readline

def is_same(paper, x, y, size):
	c = paper[x][y]

	for i in range(x, x+size):
		for j in range(y, y+size):
			if paper[i][j] != c:
					return -1
	return c


def cut(paper, x, y, size, memo):
	if size == 1:
		memo[paper[x][y]] += 1
		return

	c = is_same(paper, x, y, size)
	if c != -1:
		memo[c] += 1
		return

	half = size // 2
	cut(paper, x, y, half, memo)
	cut(paper, x, y + half, half, memo)
	cut(paper, x + half, y, half, memo)
	cut(paper, x + half, y + half, half, memo)

n = int(input())
paper = [ list(map(int, input().split())) for _ in range(n)]
memo = [0, 0]
cut(paper, 0, 0, n, memo)
print(memo[0])
print(memo[1])