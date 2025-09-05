def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    
    memo = {k: [] for k in id_list}
    r_memo = {k: 0 for k in id_list}
    already = set()
    
    for r in report:
        record = r.split()
        if r in already: continue
        r_memo[record[1]] += 1
        memo[record[1]].append(record[0])
        already.add(r)
    
    for kk, v in r_memo.items():
        if v >= k:
            for m in memo[kk]:
                idx = id_list.index(m)
                answer[idx] += 1
    return answer