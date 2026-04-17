def solution(n, k, cmd):
    prev = [i-1 for i in range(n)]
    next = [i+1 for i in range(n)]
    prev[0] = -1
    next[-1] = -1
    
    alive = ["O"] * n
    stack = []
    cur = k
    
    for c in cmd:
        if c[0] == 'U':
            for _ in range(int(c.split(" ")[1])):
                cur = prev[cur]
        elif c[0] == 'D':
            for _ in range(int(c.split(" ")[1])):
                cur = next[cur]
        elif c[0] == 'C':
            
            alive[cur] = "X"
            stack.append((cur, prev[cur], next[cur]))
            
            next[prev[cur]] = next[cur]
            prev[next[cur]] = prev[cur]
            
            if next[cur] != -1:
                cur = next[cur]
            else:
                cur = prev[cur]
        else:
            r, p, n = stack.pop()
            alive[r] = "O"
            
            if p != -1:
                next[p] = r

            if n != -1:
                prev[n] = r
            
    
    return ''.join(alive)