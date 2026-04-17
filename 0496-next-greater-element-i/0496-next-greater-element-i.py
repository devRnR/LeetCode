class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        memo = { k : -1 for k in nums2}
        answer = [-1] * len(nums1)

        for i, n2 in enumerate(nums2):

            while stack and stack[-1] < n2:
                j = stack.pop()
                memo[j] = n2
            
            stack.append(n2)
        
        for i, n1 in enumerate(nums1):
            answer[i] = memo[n1]

        return answer