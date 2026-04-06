from math import ceil
from collections import deque

def solution(progresses, speeds):
    
    release = [ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    deploy = []
    
    std = release[0]
    cnt = 1
    for i in range(1, len(progresses)):
        if release[i] <= std:
            cnt += 1
        else:
            deploy.append(cnt)
            cnt = 1
            std = release[i]

    deploy.append(cnt)
    return deploy