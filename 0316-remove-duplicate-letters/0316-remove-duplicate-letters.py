class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        check = set()
        stack = []
        memo = {}
        for c in s:
            memo[c] = memo.get(c, 0) + 1

        for c in s:

            memo[c] -= 1 

            if c in check:
                continue

            while stack and stack[-1] > c and memo[stack[-1]]> 0:
                v = stack.pop()
                check.remove(v)

            check.add(c)
            stack.append(c)

        return "".join(stack)