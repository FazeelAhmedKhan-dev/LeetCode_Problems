class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        sort_nums = sorted(nums)
        print(sort_nums)

        val = sort_nums[0]
        count = 1
        max_seq = 1

        for num in range(1, len(sort_nums)):
            if sort_nums[num] == sort_nums[num-1]:
                continue
            if sort_nums[num] == val+1:
                count += 1
            else:
                max_seq = max(max_seq, count)
                count = 1
            val = sort_nums[num]
        
        return max(max_seq, count)
