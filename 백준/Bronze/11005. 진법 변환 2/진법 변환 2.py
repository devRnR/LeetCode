import sys

input = sys.stdin.readline
answer = 0

n, k = map(int, input().split())

def marking(n):
	if n >= 10:
		return str(chr(n + 55))
	return str(n)

def decimal(n, k):
	if n < k:
		return marking(n)

	m = n // k
	r = n % k
	return decimal(m, k) + marking(r)

print(decimal(n, k))
