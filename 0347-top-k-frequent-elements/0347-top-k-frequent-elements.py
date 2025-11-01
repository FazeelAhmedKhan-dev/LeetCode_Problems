class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for i in nums:
            count[i] = 1 + count.get(i, 0)
        for n , c in count.items():
            freq[c].append(n)

        result = []

        for c in range(len(freq) -1, 0, -1):
            for n in freq[c]:
                result.append(n)

                if len(result) == k:
                    return result