def solution(genres, plays):
    gp = {}
    pd = {}
    
    for g, p in zip(genres, plays):
        pd[g] = []
        gp[g] = gp.get(g, 0) + p
        
    for i, e in enumerate(zip(genres, plays)):
        pd[e[0]].append([i, e[1]])
        
    for i, v in pd.items():
        pd[i] = list(map(lambda x: x[0], sorted(v, key = lambda x: (-x[1], x[0]))))
        
    answer = []
    for genre in list(map(lambda x: x[0], sorted(gp.items(), key = lambda x: -x[1]))):
        answer += pd[genre][:2]
    
    return answer