class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) != 1:
            n = len(nums)
            newNums = [0] * (n - 1)
            for i in range(n-1):
                val = (nums[i] + nums[i+1]) % 10
                newNums[i] = val
            nums = newNums.copy()
        return nums[0]