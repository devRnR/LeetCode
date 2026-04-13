import sys

input = sys.stdin.readline

n, k = map(int, input().split())
digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

res = []
while n > 0:
    n, r = divmod(n, k)
    res.append(digits[r])

print("".join(reversed(res)))
