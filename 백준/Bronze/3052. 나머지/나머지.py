import sys

my_input = sys.stdin.readline

N = 10
arr = { int(my_input()) % 42 for _ in range(N)}

print(len(arr))