import sys

my_input = sys.stdin.readline

def is_pair(ch, last_ch):
	if ch == ")":
		return last_ch == "("

	return last_ch == "["

while True:
	word = my_input().rstrip()

	if word == ".":
		break

	stack = []
	is_stable = 'yes'
	for ch in word:
		if ch == "(" or ch == "[":
			stack.append(ch)

		if ch == ")" or ch == "]":
			if not stack or not is_pair(ch, stack[-1]):
				is_stable = 'no'
				break

			stack.pop()

	if stack:
		is_stable = 'no'

	print(is_stable)

