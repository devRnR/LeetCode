def solution(arr1, arr2):
    r1, c1 = len(arr1), len(arr1[0])
    r2, c2 = len(arr2), len(arr2[0])
    
    answer = [[0] * c2 for _ in range(r1)]
    
    for r in range(r1):
        for k in range(c2):
            for w in range(r2):
                answer[r][k] += arr1[r][w] * arr2[w][k]
    
    return answer