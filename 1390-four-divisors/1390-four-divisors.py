import math
from typing import List

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0

        for num in nums:
            div_sum = 0
            count = 0

            for i in range(1, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    d1 = i
                    d2 = num // i

                    count += 1
                    div_sum += d1

                    if d1 != d2:
                        count += 1
                        div_sum += d2

                    if count > 4:
                        break

            if count == 4:
                ans += div_sum

        return ans
