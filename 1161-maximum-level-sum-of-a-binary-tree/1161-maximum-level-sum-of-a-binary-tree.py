from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        max_sum = [float('-inf'), 0]
        queue = deque([root])
        level = 1

        while queue:

            level_size = len(queue)
            curr_sum = 0

            for _ in range(level_size):

                node = queue.popleft()
                curr_sum += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            
            if curr_sum > max_sum[0]:
                max_sum[0], max_sum[1] = curr_sum, level

            level += 1
        
        return max_sum[1]

