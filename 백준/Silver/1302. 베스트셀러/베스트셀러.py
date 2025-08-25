import sys

my_input = sys.stdin.readline


n = int(my_input())

books = [my_input().strip() for _ in range(n)]
memo = {}
top_level = 0

for key in books:
	if key in memo:
		memo[key] = memo[key] + 1
	else:
		memo[key] = 1

max_cnt = max(memo.values())
extract = [k for k, v in memo.items() if v == max_cnt]
sorted_extract = sorted(extract)

print(sorted_extract[0])

