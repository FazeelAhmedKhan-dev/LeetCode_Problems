# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        # Split into left and right parts
        right_start = len(preorder)
        for i in range(1, len(preorder)):
            if preorder[i] > root_val:
                right_start = i
                break
        
        left_part = preorder[1:right_start]
        right_part = preorder[right_start:]
        
        root.left = self.bstFromPreorder(left_part)
        root.right = self.bstFromPreorder(right_part)
        
        return root