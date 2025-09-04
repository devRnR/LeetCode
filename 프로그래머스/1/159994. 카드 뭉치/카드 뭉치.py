from collections import deque
def solution(cards1, cards2, goal):
    c1 = deque(cards1)
    c2 = deque(cards2)
    answer = 'Yes'

    for w in goal:
        if c1 and w == c1[0]:
            c1.popleft()
        elif c2 and w == c2[0]:
            c2.popleft()
        else:
            answer = 'No'
            break
    
    return answer