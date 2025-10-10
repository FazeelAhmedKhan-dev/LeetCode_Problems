class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for _ in range(len(nums)):
            if nums[i] == 0:
                val = nums.pop(i)
                nums.append(val)
            else:
                i += 1
        