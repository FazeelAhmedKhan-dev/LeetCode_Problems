from functools import lru_cache

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:

        m = len(nums1)
        n = len(nums2)

        @lru_cache(None)
        def solve(i, j):
            if i == m or j == n:
                return float('-inf')
            
            p1 = nums1[i] * nums2[j]
            p2 = (nums1[i] * nums2[j]) + solve(i+1, j+1)
            p3 = solve(i, j+1)
            p4 = solve(i+1, j)

            return max(p1, p2, p3, p4)
        
        return solve(0, 0)
        