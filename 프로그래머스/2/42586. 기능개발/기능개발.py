from math import ceil
from collections import deque

def solution(progoresses, speeds):
    
    q = deque(zip(progoresses, speeds))
    deploy = []

    while q:
        cnt = 1
        
        p, s = q.popleft()
        m = ceil((100 - p ) / s)
        
        while q and (q[0][1] * m + q[0][0]) >= 100:
            cnt += 1
            q.popleft()

        deploy.append(cnt)

    return deploy