from collections import deque
def solution(progresses, speeds):
    answer = []
    pq = deque([ list(ps) for ps in zip(progresses, speeds)])
    goal = 100
    while pq:
        p = pq[0]
        
        progress = p[0]
        speed = p[1]
        
        remain = goal - progress 
        remain_days =  remain // speed + (1 if remain % speed else 0)
        
        for e in pq:
            e[0] += remain_days * e[1]
        
        cnt = 0
        while pq:
            e = pq.popleft()
            
            if e[0] < goal:
                pq.appendleft(e)
                break
            
            cnt += 1
        
        answer.append(cnt)
        
    return answer
