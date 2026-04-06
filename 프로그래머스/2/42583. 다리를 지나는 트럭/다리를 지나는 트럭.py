from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    front = 0
    time = 0
    
    cur_w = 0
    brg = deque()
    tq = deque(truck_weights)
    
    while tq or brg:

        for b in brg:
            b[1] += 1
        
        if brg and brg[0][1] == bridge_length:
            w, t = brg.popleft()
            cur_w -= w

        if tq and cur_w + tq[0] <= weight:
            tw = tq.popleft()
            cur_w += tw
            brg.append([tw, 0])        
        
        time += 1
    
    return time