import math
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        
        divisor_sum = 0

        for num in nums:
            curr_sum = 0
            divisor_count = 0
            for i in range(1, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    curr_sum += i
                    if num // i != i:
                        curr_sum += num // i
                        divisor_count += 1
                        
                    divisor_count += 1

            if divisor_count == 4:
                divisor_sum += curr_sum
        
        return divisor_sum

