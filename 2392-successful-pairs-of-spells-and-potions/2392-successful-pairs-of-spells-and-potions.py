class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        pairs = []
        potions.sort()

        for spell in spells:
            index = len(potions)
            l,r = 0, len(potions) - 1
            while l <= r:
                mid = (r + l) // 2
                if spell * potions[mid] >= success:
                    index = mid
                    r = mid - 1
                else:
                    l = mid + 1
            pairs.append(len(potions) - index)
        return pairs