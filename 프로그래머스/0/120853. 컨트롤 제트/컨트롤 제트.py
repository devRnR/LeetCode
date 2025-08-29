def solution(s):
    answer = 0
    for i, ch in enumerate(arr := s.split(" ")):
        if ch == 'Z':
            answer -= int(arr[i-1])
        else:
            answer += int(ch)
    return answer