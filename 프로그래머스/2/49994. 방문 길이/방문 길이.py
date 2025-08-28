
def solution(dirs):
    N, M = 21, 21
    x,y = 10, 10
    
    map = [[0 for _ in range(M)] for _ in range(N)]
    map[y][x] = 1
    
    command = {
        "U": (0, -1),
        "D": (0, 1),
        "R": (1, 0),
        "L": (-1, 0)
    }
    
    cnt = 0
    for dir in dirs:
        next_move = command[dir]
        
        ny = y + 2 * next_move[1]
        nx = x + 2 * next_move[0]
        ny_edge = y + next_move[1]
        nx_edge = x + next_move[0]
        
        if ny >= N or ny < 0: continue
        if nx >= M or nx < 0: continue
        if map[ny_edge][nx_edge] == 0:
            cnt += 1
        
        map[ny][nx] = 1
        map[ny_edge][nx_edge] = 1
        x = nx
        y = ny
    
    return cnt