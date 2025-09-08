class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        duplicate = set()

        left = 0

        for right in range(len(nums)):
            if right - left > k:
                duplicate.remove(nums[left])
                left += 1
            if nums[right] in duplicate:
                return True
            duplicate.add(nums[right])
        return False