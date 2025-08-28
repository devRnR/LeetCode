def solution(arr1, arr2):
    arr2_zipped = list(zip(*arr2))
    return [[sum( a*b for a, b in zip(row, row2)) for row2 in arr2_zipped] for row in arr1]