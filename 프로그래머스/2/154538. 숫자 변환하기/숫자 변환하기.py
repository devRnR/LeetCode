from collections import deque

def bfs(x,y,n,memo):
    q = deque()
    q.append(x)
    
    while q:
        v = q.popleft()
        
        if v == y:
            return memo[v]
        
        v1 = v + n
        v2 = v * 2
        v3 = v * 3
        
        if v1 <= y and memo[v1] == 0:
            memo[v1] = memo[v] + 1
            q.append(v1)
            
        if v2 <= y and memo[v2] == 0: 
            memo[v2] = memo[v] + 1
            q.append(v2)
            
        if v3 <= y and memo[v3] == 0: 
            memo[v3] = memo[v] + 1
            q.append(v3)
        

def solution(x, y, n):
    
    if x == y: return 0

    answer = 0
    memo = [0] * (y+1)
    
    answer = bfs(x,y,n,memo)
    
    return answer if answer else -1

        
