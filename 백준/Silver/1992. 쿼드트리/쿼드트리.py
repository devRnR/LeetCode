import sys

input = sys.stdin.readline


def is_same(paper, x, y, size):
	target = paper[x][y]

	for i in range(x, x+size):
		for j in range(y, y+size):
			if paper[i][j] != target:
				return -1

	return target


def compact(paper, x, y, size):
	if size == 1:
		return str(paper[x][y])

	s = is_same(paper, x, y, size)
	if s != -1:
		return str(s)

	half = size //2

	tl = compact(paper, x, y, half)
	tr = compact(paper, x, y+half, half)
	bl = compact(paper, x+half, y, half)
	br = compact(paper, x+half, y+half, half)

	return "(" + "".join([tl, tr, bl, br]) + ")"


n = int(input())
paper = [ list(map(int, input().strip())) for _ in range(n)]
print(compact(paper, 0, 0, n))