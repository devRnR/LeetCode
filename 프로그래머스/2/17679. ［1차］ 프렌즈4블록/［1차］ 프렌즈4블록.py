def marking_square(m, n, board, memo):
    for i in range(m-1):
        for j in range(n-1):
            if board[i][j] == "0": continue
            if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                memo[i][j] = "-"
                memo[i][j+1] = "-"
                memo[i+1][j] = "-"
                memo[i+1][j+1] = "-"
    return (board, memo)

def clear_memo(m, n):
    return [[0 for _ in range(n)] for _ in range(m)]

def cnt_sqaure(m, n, memo):
    cnt = 0
    for i in range(m):
        for j in range(n):
            if memo[i][j] == "-":
                cnt += 1
                
    return cnt

def clear_board(m, n, board, memo):
    for i in range(m):
        for j in range(n):
            if memo[i][j] == "-":
                board[i][j] = "0"
    
    for j in range(n):
        for i in range(m-1, -1, -1):
            if board[i][j] == "0": continue
            start = i
                
            while start + 1 < m:
                if board[start+1][j] == "0":
                    board[start+1][j] = board[start][j]
                    board[start][j] = "0"
                else:
                    break
                start += 1
    return board
    

def solution(m, n, board):
    answer = 0
    board = [list(row) for row in board]
    memo = [[0 for _ in range(n)] for _ in range(m)]
    
    while True:
        board, memo = marking_square(m, n, board, memo)
        cnt = cnt_sqaure(m, n, memo)
        
        if cnt == 0:
            break
        
        board = clear_board(m, n, board, memo)
        memo = clear_memo(m, n)
        answer += cnt
        
            
    return answer


'''
문제는 브루투포스 문제인 것 같음

핵심은 현재 위치에서 4개의 블록을 만들 수 있는지가 관건

어떻게 4개인것을 판단할 것인가?

하나의 기준 오->아->왼 의 순서로 일단 1차로 부실 수 있는 것을 확인한다.
- 범위를 벗어나는 건지 확인이 필요하다.

만약 부신게 있다면 위에 블록을 아래로 내려주어야 한다

하나의 row를 stack으로 바라볼 수 있다면 어떨까?
아래로 살피면서 중간에 지워진게 있다면 다른 걸로 채울 수 있도록 해야할 듯

flag를 통해서 부실 수 있는 것을 모두 부셨는지 확인하자


'''