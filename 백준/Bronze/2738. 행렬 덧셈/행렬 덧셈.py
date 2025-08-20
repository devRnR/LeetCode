import sys

my_input = sys.stdin.readline

N, M = list(map(int, my_input().split()))

A = [ list(map(int, my_input().split())) for _ in range(N)]
B = [ list(map(int, my_input().split())) for _ in range(N)]

answer = [ [0 for _ in range(M)] for _ in range(N)]

for i in range(N):
	for j in range(M):
		answer[i][j] = A[i][j] + B[i][j]


for row in answer:
	print(*row,sep=" ")
