
def solution(dirs):
    x, y = 0, 0
    
    memo = set()
    command = {
        "U": (0, 1),
        "D": (0, -1),
        "R": (1, 0),
        "L": (-1, 0)
    }
    
    for dir in dirs:
        ny = y + command[dir][1]
        nx = x + command[dir][0]
        
        if ny <= 5 and ny >= -5 and nx <= 5 and nx >= -5:
            memo.add((x,y,nx,ny))
            memo.add((nx,ny,x,y))
            x = nx
            y = ny
    
    return len(memo)//2