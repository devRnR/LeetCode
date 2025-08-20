import sys

my_input = sys.stdin.readline


N, X = list(map(int, my_input().split()))
arr = list(map(int, my_input().split()))

answer = [x for x in arr if x < X]
print(*answer,sep=' ')
