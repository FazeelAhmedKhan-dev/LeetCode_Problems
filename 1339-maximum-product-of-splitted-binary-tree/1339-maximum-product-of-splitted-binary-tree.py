# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_product = 0
        self.total_sum = 0

    def sum_of_tree(self, root):
        if not root:
            return 0   
        left = self.sum_of_tree(root.left)
        right = self.sum_of_tree(root.right)
        
        return root.val + left + right
    
    def find_max(self, root):
        if not root:
            return 0
        
        left = self.find_max(root.left)
        right = self.find_max(root.right)
        subTreeSum = root.val + left + right
        
        remainingSubTreeSum = self.total_sum - subTreeSum
        self.max_product = max(self.max_product, subTreeSum*remainingSubTreeSum)

        return subTreeSum


    def maxProduct(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        self.total_sum = self.sum_of_tree(root)
        self.find_max(root)

        return self.max_product % 1000000007

        