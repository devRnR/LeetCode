from math import ceil

def solution(progoresses, speeds):
    days = [ceil((100-p)/s) for p, s in zip(progoresses, speeds)]
    answer = []
    
    cur = days[0]
    cnt = 0
    
    for d in days:
        if d <= cur:
            cnt += 1
        else:
            answer.append(cnt)
            cur = d
            cnt = 1
    
    answer.append(cnt)

    return answer