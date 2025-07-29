class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # running_nums = []

        # for i in range(len(nums)):
        #     if not running_nums:
        #         running_nums.append(nums[i])
        #         continue
        #     running_nums.append(nums[i] + running_nums[i-1])
        
        # return running_nums

        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums