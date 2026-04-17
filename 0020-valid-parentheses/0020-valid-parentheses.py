class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for ch in s:
            if not stack or ch in '({[':
                stack.append(ch)
            else:
                top = stack[-1]

                if ch == ')' and top == '(':
                    stack.pop()
                elif ch == '}' and top == '{':
                    stack.pop()
                elif ch == ']' and top == '[':
                    stack.pop()
                else:
                    return False

        return not stack

            