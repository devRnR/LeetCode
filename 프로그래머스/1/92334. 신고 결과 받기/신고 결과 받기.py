def solution(id_list, report, k):
    ban = {}
    id = {k: i for i, k in enumerate(id_list)}
    answer = [0 for _ in range(len(id_list))]
    
    for r in report:
        f, t = r.split()
        if t in ban:
            ban[t].add(f)
        else:
            ban[t] = {f,}

    for _, v in ban.items():
        if len(v) >= k:
            for w in v:
                answer[id[w]] += 1
    
    return answer