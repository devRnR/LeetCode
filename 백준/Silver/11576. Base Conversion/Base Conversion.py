import string
import sys

my_input = sys.stdin.readline

A, B = map(int, my_input().split())
m = int(my_input())
arr = list(map(int, my_input().split()))[::-1]


def convert_to_10(nums):
	numbers = 0

	for i in range(m):
		numbers += nums[i] * (A ** i)

	return numbers

def convert(n, b):
	if n < b:
		return [n]

	quo = n // b
	rem = n % b

	return convert(quo, b) + [rem]


res = convert_to_10(arr)
res2 = convert(res, B)

print(" ".join(map(str, res2)))

