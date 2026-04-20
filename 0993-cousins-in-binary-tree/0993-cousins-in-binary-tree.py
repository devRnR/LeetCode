from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        # 1. level과 부모를 찾기
        # 2. level이 같으면서 부모가 다른지

        q = deque([root])
        x_level = 0
        y_level = 0
        x_parent = 0
        y_parent = 0

        level = 0
        while q:
            level_size = len(q)

            for _ in range(level_size):
                node = q.popleft()

                if node.val == x:
                    x_level = level
                
                if node.val == y:
                    y_level = level

                if node.left:
                    q.append(node.left)

                    if node.left.val == x:
                        x_parent = node.val
                    elif node.left.val == y:
                        y_parent = node.val

                if node.right:
                    q.append(node.right)

                    if node.right.val == y:
                        y_parent = node.val
                    elif node.right.val == x:
                        x_parent = node.val
                
            level += 1


        return x_level == y_level and x_parent != y_parent



        