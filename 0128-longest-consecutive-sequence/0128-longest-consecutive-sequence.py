class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:

                currLength = 0
                
                while (num + currLength) in numSet:
                    currLength += 1

                longest = max(longest, currLength)
        
        return longest
