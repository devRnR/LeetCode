from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        q = deque()
        q.append([root])
        answer =[]

        while q:
            nodes = q.popleft()
            temp = []
            new_nodes = []
            for node in nodes:
                if node:
                    temp.append(node.val)
                    if node.left:
                        new_nodes.append(node.left)
                    if node.right:
                        new_nodes.append(node.right)
            
            if new_nodes:
                q.append(new_nodes)
            
            if temp:
                answer.append(temp)
        
        return answer
        