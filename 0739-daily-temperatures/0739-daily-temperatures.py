class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        answer = [0] * n

        for i, t in enumerate(temperatures):

            while stack and temperatures[stack[-1]] < t:
                prev_t = stack.pop()
                answer[prev_t] = i - prev_t
            
            stack.append(i)

        return answer
        