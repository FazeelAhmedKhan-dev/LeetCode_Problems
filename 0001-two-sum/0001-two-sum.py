class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        num_dict = {}

        for i in range(len(nums)):
            val = target - nums[i]

            if val in num_dict:
                return [i, num_dict[val]]
            
            num_dict[nums[i]] = i