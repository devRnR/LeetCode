def solution(genres, plays):
    
    gd = {k: 0 for k in set(genres)}
    sd = {k: [] for k in set(genres)}
    answer = []
    
    for i,v in enumerate(zip(genres, plays)):
        gd[v[0]] += v[1]
        sd[v[0]].append((i, v[1]))
    
    g_sorted = sorted(gd.items(), key = lambda x: -x[1])
    
    for k, v in sd.items():
        sd[k] = sorted(v, key = lambda x: (-x[1], x[1]))
    
    for k, _ in g_sorted:
        answer += list(map(lambda x: x[0], sd[k][:2]))
    
    return answer