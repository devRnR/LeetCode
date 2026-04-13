def solution(id_list, report, k):
    ban = {r.split()[1]: 0 for r in report}
    answer = [0 for _ in range(len(id_list))]
    
    for r in set(report):
        ban[r.split()[1]] += 1
        
    for r in set(report):
        if ban[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1
    
    return answer