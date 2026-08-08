class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height:
            return 0
        
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]

        maxWater = 0

        while l < r:
            
            minVal = min(maxL, maxR)

            if minVal == maxL:
                l += 1
                trapWater = minVal - height[l]

                if trapWater >= 0:
                    maxWater += trapWater
                
                maxL = max(maxL, height[l])

            else:
                r -= 1
                
                trapWater = minVal - height[r]

                if trapWater >= 0:
                    maxWater += trapWater
                
                maxR = max(maxR, height[r])
        
        return maxWater
            


