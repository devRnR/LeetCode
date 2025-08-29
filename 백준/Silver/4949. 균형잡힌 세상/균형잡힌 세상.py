import sys

my_input = sys.stdin.readline

while True:
	word = my_input().rstrip()

	if word == ".":
		break

	stack = []
	is_stable = 'yes'
	for ch in word:
		if ch == "(" or ch == "[":
			stack.append(ch)

		if ch == ")":
			if len(stack) == 0 or stack[-1] != "(":
				is_stable = 'no'
				break
			stack.pop()

		if ch == "]":
			if len(stack) == 0 or stack[-1] != "[":
				is_stable = 'no'
				break
			stack.pop()

	if len(stack) > 0:
		is_stable = 'no'

	print(is_stable)
