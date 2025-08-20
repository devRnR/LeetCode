import sys

my_input = sys.stdin.readline

N = int(my_input())
answer = 0

for _ in range(N):
	word = list(my_input().strip())
	d = {word[0]: True}

	is_group_word = True
	for i in range(1, len(word)):
		if word[i] != word[i - 1]:
			if word[i] in d:
				is_group_word = False

		d[word[i]] = True

	if is_group_word:
		answer += 1

print(answer)
