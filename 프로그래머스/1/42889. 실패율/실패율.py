def solution(N, stages):
    memo = {k:0.0 for k in range(1, N+1)}
    cnt = [0 for _ in range(N+2)]
    reached_player = len(stages)
    
    for stage in stages:
        cnt[stage] += 1
    
    for i in range(1, len(cnt) - 1):
        memo[i] = cnt[i] / reached_player
        reached_player -= cnt[i]
        
        if reached_player == 0:
            break
    
    return [k for k, _ in sorted(memo.items(), key=lambda x: (-x[1], x[1]))]