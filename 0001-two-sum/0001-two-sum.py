class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        result = []
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                sum_target = nums[i] + nums[j]

                if sum_target == target:
                    return [i , j]