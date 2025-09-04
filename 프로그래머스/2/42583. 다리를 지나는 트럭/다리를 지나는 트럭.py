from collections import deque

def solution(bridge_length, weight, truck_weights):
    trucks = deque(truck_weights)
    bridge = deque()
    
    time = 1
    nw = 0
    while trucks or bridge:
        
        if bridge:
            time = max(time, bridge[0][1])
        
        while bridge:
            if time - bridge_length == bridge[0][1]:
                pt = bridge.popleft()
                nw -= pt[0]
            else:
                break

        if trucks and nw + trucks[0] <= weight and len(bridge) < bridge_length:
            t = trucks.popleft()
            bridge.append((t, time))
            nw += t
            
        time += 1
    return time - 1