import sys

input = sys.stdin.readline

def z(n, tx, ty):
	if n == 0:
		return 0

	half = 2 ** (n -1)
	area = half * half

	if tx < half and ty < half:
		return z(n-1, tx, ty)
	elif tx < half and ty >= half:
		return area + z(n-1, tx, ty - half)
	elif tx >= half and ty < half:
		return 2*area + z(n-1, tx - half, ty)
	else:
		return 3*area + z(n-1, tx - half, ty - half)


n, tx, ty = map(int, input().split())
print(z(n, tx, ty))
