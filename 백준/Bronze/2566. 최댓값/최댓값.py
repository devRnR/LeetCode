import sys

my_input = sys.stdin.readline


N = 9
M = 9

arr = [list(map(int, my_input().split())) for _ in range(N)]

max_i = 0
max_j = 0
max_value = 0

# O(N)
for i in range(N):
	for j in range(M):
		if max_value < arr[i][j]:
			max_value = arr[i][j]
			max_i = i
			max_j = j

print(max_value)
print(max_i + 1 , max_j + 1)
