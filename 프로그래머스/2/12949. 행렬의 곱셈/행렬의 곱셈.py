def solution(arr1, arr2):
	ax = len(arr1)
	bx = len(arr2)
	by = len(arr2[0])

	answer = [[0 for _ in range(by)] for _ in range(ax)]

	for i in range(ax):
		for j in range(by):
			for k in range(bx):
				answer[i][j] += arr1[i][k] * arr2[k][j]

	return answer