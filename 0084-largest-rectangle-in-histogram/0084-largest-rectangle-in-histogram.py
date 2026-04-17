class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            start = i
            
            while stack and stack[-1][1] > h:
                idx, prev_h = stack.pop()
                max_area = max(max_area, (i - idx) * prev_h)
                start = idx
            
            stack.append((start, h))
        
        for i, h in stack:
            max_area = max(max_area, (n - i) * h)
        
        return max_area
