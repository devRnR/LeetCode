import sys

my_input = sys.stdin.readline

N = int(my_input())
arr = [sum(map(int, my_input().split())) for _ in range(N)]

print(*arr, sep="\n")
