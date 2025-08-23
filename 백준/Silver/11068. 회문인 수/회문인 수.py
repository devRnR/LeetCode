import string
import sys

my_input = sys.stdin.readline

T = int(my_input())


def convert(n, b):
	digits = string.digits + string.ascii_uppercase + string.ascii_lowercase + "+/"

	if n < b:
		return digits[n]

	quo = n // b
	rem = n % b

	return convert(quo, b) + digits[rem]



def palindrome(n, i, j):

	if i > j:
		return True

	if n[i] != n[j]:
		return False

	return palindrome(n, i+1, j-1)

for _ in range(T):
	N = int(my_input())

	res = False

	for base in range(2, 65):
		converted = convert(N, base)
		res = palindrome(converted, 0, len(converted) - 1)

		if res:
			break

	if res:
		print(1)
	else:
		print(0)
