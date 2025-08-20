import sys

my_input = sys.stdin.readline

N = 10
answer = set()

for _ in range(N):
	answer.add(int(my_input()) % 42)

print(len(answer))