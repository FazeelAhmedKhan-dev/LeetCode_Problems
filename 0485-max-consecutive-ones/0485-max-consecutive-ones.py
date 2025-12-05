class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        curr_sum = 0
        max_sum = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                left = right+1
                continue
            curr_sum = len(nums[left:right+1])
            max_sum = max(curr_sum, max_sum)

        return max_sum