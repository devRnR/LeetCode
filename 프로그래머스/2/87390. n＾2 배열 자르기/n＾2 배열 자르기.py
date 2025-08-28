def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        p = i // n + 1
        m = i % n + 1
        
        answer += [max(p,m)]
        
    return answer