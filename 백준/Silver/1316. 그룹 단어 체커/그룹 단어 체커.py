import sys

input = sys.stdin.readline
answer = 0

for _ in range(int(input())):
	n = input()
	check = {}
	cur_c = n[0]
	flag = False

	for i in range(1, len(n)):
		if n[i] == cur_c:
			continue
		
		if n[i] in check:
			flag = True
			break

		check[cur_c] = 1
		cur_c = n[i]

	if not flag: answer += 1

print(answer)
