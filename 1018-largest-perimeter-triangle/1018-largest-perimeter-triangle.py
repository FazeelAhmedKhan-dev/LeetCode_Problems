class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        ans = 0
        nums_sorted = nums.sort()

        for i in range(len(nums)-1, 1, -1):
            if nums[i-1] + nums[i-2] > nums[i]:
                perimeter = nums[i] + nums[i-1] + nums[i-2]
                ans = max(ans, perimeter)

        return ans