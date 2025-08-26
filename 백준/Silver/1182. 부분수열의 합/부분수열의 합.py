import sys

def powerset(s):
	masks = [1 << i for i in range(len(s))]

	for i in range(1 << len(s)):
		yield [ss for ss, mask in zip(s, masks) if mask & i]

my_input = sys.stdin.readline

N, S = map(int, my_input().split())
arr = list(map(int, my_input().split()))

answer = 0
for power in powerset(arr):
	if len(power) == 0:
		continue

	if sum(power) == S:
		answer += 1

print(answer)