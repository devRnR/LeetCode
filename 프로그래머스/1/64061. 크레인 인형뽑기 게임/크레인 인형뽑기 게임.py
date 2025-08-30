from collections import deque
def solution(board, moves):
    new_board = [deque(filter( lambda x: x!= 0, c)) for c in zip(*board)]
    stack = []
    answer = 0
    
    for m in moves:
        line = new_board[m-1]
        if len(line) == 0:
            continue
        
        got =line.popleft()
        
        if stack[-1:] == [got]:
            stack.pop()
            answer += 2
        else:
            stack.append(got)
        
    return answer