class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        
        repeated = set()

        for i in nums:
            if i in repeated:
                return i
            repeated.add(i)
        