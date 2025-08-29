def solution(s):
    cnt = 0
    for i in range(len(s)):
        stack = []
        is_pair = False
        
        for ch in s:
            if ch == ')' or ch == ']' or ch == '}':
                if not stack:
                    is_pair = False
                    break
                
                if ch == ')' and stack[-1] == '(':
                    stack.pop()
                elif ch == ']' and stack[-1] =='[':
                    stack.pop()
                elif ch == '}' and stack[-1] =='{':
                    stack.pop()
                else:
                    is_pair = False
                    break
            else:
                stack.append(ch)
                is_pair = True
                    
        cnt += 1 if is_pair and not stack else 0
        s = s[1:] + s[0]
    return cnt