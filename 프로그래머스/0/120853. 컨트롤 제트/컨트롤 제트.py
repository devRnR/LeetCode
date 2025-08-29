def solution(s):
    answer = 0
    arr = s.split(" ")
    for i, ch in enumerate(arr):
        if ch == 'Z':
            answer -= int(arr[i-1])
        else:
            answer += int(ch)
    return answer