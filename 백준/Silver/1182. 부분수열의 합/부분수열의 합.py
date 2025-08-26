import sys
from itertools import combinations, chain

my_input = sys.stdin.readline

N, S = map(int, my_input().split())
arr = list(map(int, my_input().split()))
answer = 0

for i in chain.from_iterable(combinations(arr, r) for r in range(1, N+1)):
	if sum(i) == S:
		answer += 1

print(answer)
