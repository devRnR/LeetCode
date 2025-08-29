def solution(s):
    answer = 0
    stack = []
    
    for ch in s:
        if stack[-1:] == [ch]:
            stack.pop()
        else:
            stack.append(ch)
            
    return 0 if len(stack) else 1