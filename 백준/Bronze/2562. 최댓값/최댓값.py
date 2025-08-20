import sys

my_input = sys.stdin.readline

N = 9

max_value = float('-inf')
max_index = 0

for i in range(9):
	num = int(my_input())
	if max_value < num:
		max_value = num
		max_index = i

print(max_value)
print(max_index + 1)
