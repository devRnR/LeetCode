class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        answer = [-1] * len(nums1)

        for i, n1 in enumerate(nums1):
            stack.append((i, nums2.index(n1)))

        while stack:
            i, s = stack.pop()
            for j in range(s+1, len(nums2)):
                if nums1[i] < nums2[j]:
                    answer[i] = nums2[j]
                    break
        return answer