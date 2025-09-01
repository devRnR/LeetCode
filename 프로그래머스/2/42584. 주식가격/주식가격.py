# from collections import deque
# def solution(prices):
#     result = []
#     queue = deque(prices)
    
#     while queue:
#         period = 0
#         price = queue.popleft()
        
#         for after in queue:
#             period += 1
#             if price > after:
#                 break
                
#         result.append(period)
        
#     return result

def solution(prices):
    n = len(prices)
    stack = [0]
    answer = [0]  * n
    
    for i in range(1, n):
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        
        stack.append(i)
    
    while stack:
        j = stack.pop()
        answer[j] = n - 1 - j
        
    return answer
    