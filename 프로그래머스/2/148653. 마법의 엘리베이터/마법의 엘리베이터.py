def solution(storey):
    answer = 0
    
    while storey:
        d = storey % 10
        storey //= 10
        if d == 5:
            if storey % 10 >= 5:
                storey += 1
                answer += 10 - d
            else:
                answer += d
        elif d < 5:
            answer += d
        else:
            storey += 1
            answer += 10 - d
                
    return answer