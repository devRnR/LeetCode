from collections import deque
def solution(cards1, cards2, goal):
    g = deque(goal)
    c1 = deque(cards1)
    c2 = deque(cards2)
    
    while g:
        w = g.popleft()
        
        if c1 and c1[0] == w:
            c1.popleft()
        elif c2 and c2[0] == w:
            c2.popleft()
        else:
            g.append(w)
            break
    
    return 'No' if len(g) else 'Yes'