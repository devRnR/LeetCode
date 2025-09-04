from collections import deque
from math import ceil

def solution(progresses, speeds):
    answer = []
    pq = deque([ list(ps) for ps in zip(progresses, speeds)])
    goal = 100
    while pq:
        remain = goal - pq[0][0]
        remain_days =  ceil((100 - pq[0][0]) / pq[0][1])
        
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
