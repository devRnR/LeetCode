from collections import deque

def solution(n, k, cmd):
    
    deleted = []
    
    up = [i - 1 for i in range(n + 2)]
    down = [i + 1 for i in range(n + 1)]
    
    k += 1
    
    for c in cmd:
        if c.startswith("C"):
            deleted.append(k)
            
            up[down[k]] = up[k]
            down[up[k]] = down[k]
            
            k = up[k] if n < down[k] else down[k]
            
        elif c.startswith("Z"):
            z = deleted.pop()
            
            down[up[z]] = z
            up[down[z]] = z
        else:
            
            a, x = c.split()
            
            if a == 'U':
                x = int(x)
                while x > 0:
                    k = up[k]
                    x -= 1
            else:
                x = int(x)
                while x > 0:
                    k = down[k]
                    x -= 1            
    answer = ['O'] * n
    for i in deleted:
        answer[i - 1] = 'X'
    
    return "".join(answer)