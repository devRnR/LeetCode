import sys

my_input = sys.stdin.readline

n = int(my_input().strip())


def convert_bite(n):

	if n // 2 == 0:
		return n

	quo = n // 2
	rem = n % 2

	return str(convert_bite(quo)) + str(rem)


print(convert_bite(n))