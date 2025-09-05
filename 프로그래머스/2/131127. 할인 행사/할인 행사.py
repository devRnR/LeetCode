from copy import copy
from collections import Counter
def solution(want, number, discount):
    # days = []
    
#     for i in range(0, len(discount) - 10 + 1):
#         memo = {}
#         for j in range(i, i + 10):
#             memo[discount[j]] = memo.get(discount[j], 0) + 1
#         days.append(memo)

#     answer = 0
#     for idx, d in enumerate(days):
#         flag = True
#         for i, q in zip(want, number):
#             if i not in d or d[i] < q:
#                 flag = False
#                 break
        
#         if flag:
#             answer += 1
    
    memo = {}
    
    for i in range(len(want)):
        memo[want[i]] = number[i]
        
    answer = 0
    for i in range(len(discount) - 9):
        if memo == Counter(discount[i:i+10]):
            answer += 1
    return answer