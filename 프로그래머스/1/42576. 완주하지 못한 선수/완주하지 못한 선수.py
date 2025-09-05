def solution(participant, completion):
    answer = ''
    pd = {}
    
    for p in participant:
        pd[p] = pd.get(p, 0) + 1
    
    for c in completion:
        pd[c] -= 1
        
    for k, v in pd.items():
        if v > 0:
            answer = k
            break

    return answer