def solution(participant, completion):
    pd = {}
    
    for p in participant:
        pd[p] = pd.setdefault(p, 0) + 1
        
    for c in completion:
        if c in pd:
            pd[c] -= 1
        
    for k, v in pd.items():
        if v > 0:
            return k