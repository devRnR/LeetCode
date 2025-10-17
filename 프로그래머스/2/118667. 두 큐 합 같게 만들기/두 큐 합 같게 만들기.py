from collections import deque

def solution(queue1, queue2):
    d1 = deque(queue1)
    d2 = deque(queue2)
    
    left_sum = sum(d1)
    right_sum = sum(d2)

    if left_sum == right_sum: return 0

    total_sum = left_sum + right_sum
    half = total_sum // 2
    
    if total_sum % 2 != 0: return -1    

    cnt = 0
    left = d1[0]
    right = d2[0]
    
    limit = max(len(d1), len(d2)) * 3
    while True:
        if left_sum > right_sum:
            left_sum -= d1[0]
            right_sum += d1[0]
            
            d2.append(d1.popleft())
        else:
            right_sum -= d2[0]
            left_sum += d2[0]
            
            d1.append(d2.popleft())
        
        if not len(d1) or not len(d2):
            return -1
        
        cnt += 1
        if left_sum == right_sum:
            break
            
        if cnt > limit:
            return -1

    return cnt if cnt else -1


'''

서로 옮겼을 때 한번식 다 옮겨 봤는데도 못 만들면 over
'''
