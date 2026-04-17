class Solution:

    def get_max(self, arr: List[str]) -> int:
        n = len(arr)
        stack = []
        max_area = 0

        for i, a in enumerate(arr):
            start = i
            v = int(a)
            
            while stack and stack[-1][1] > v:
                idx, prev_v = stack.pop()
                max_area = max(max_area, (i - idx) * prev_v)
                start = idx
            
            stack.append((start, v))
        
        for i, v in stack:
            max_area = max(max_area, (n - i) * v)
        
        return max_area

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        row, col = len(matrix), len(matrix[0])
        heights = [0] * col
        max_area = 0

        for r in range(row):
            for c in range(col):
                if matrix[r][c] == '1':
                    heights[c] += 1
                else:
                    heights[c] = 0
            # 누적 후 heights를 바닥으로 본다.
            max_area = max(max_area, self.get_max(heights))

        return max_area