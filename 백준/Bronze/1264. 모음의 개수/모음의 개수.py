import sys

my_input = sys.stdin.readline

mo = ['a', 'e','i', 'o','u', 'A', 'E', 'I', 'O', 'U']

while True :
	word =	my_input().strip()

	if word == '#':
		break

	result = len(list(filter(lambda x: x in mo, list(word))))
	print(result)
