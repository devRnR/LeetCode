class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        area = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                pi, ph = stack.pop()
                area = max(area, (i - pi) * ph)
                start = pi

            stack.append((start, h))

        for i, h in stack:
            area = max(area, (n - i) * h)

        return area
