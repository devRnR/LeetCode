class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        check = set()
        stack = []
        last = {c:i for i, c in enumerate(s)}

        for i, c in enumerate(s):
            if c in check:
                continue

            while stack and stack[-1] > c and last[stack[-1]]> i:
                v = stack.pop()
                check.remove(v)

            check.add(c)
            stack.append(c)

        return "".join(stack)