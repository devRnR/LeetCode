def solution(arr, divisor):
    answer = sorted([a for a in arr if a % divisor == 0])
    return [-1 ]if len(answer) == 0 else answer
