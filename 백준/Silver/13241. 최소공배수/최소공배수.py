import sys

my_input = sys.stdin.readline

A, B = map(int, my_input().split())


def gcd(a,b):
	if a == 0:
		return b

	return gcd(b%a, a)

res = gcd(min(A, B), max(A, B))
answer = (A*B)/ res

print(int(answer))

