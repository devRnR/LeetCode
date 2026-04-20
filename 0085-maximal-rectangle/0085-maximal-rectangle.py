class Solution:

    def largets_rectangle_area(self, heights:List[int]) -> int:
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

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        n, m = len(matrix), len(matrix[0])
        heights = [0] * m
        area =0

        for row in matrix:
            for i, v in enumerate(row):
                if int(v):
                    heights[i] += 1
                else:
                    heights[i] = 0
            area = max(area, self.largets_rectangle_area(heights))

        return area