class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        remainder = 1
        length = 1

        seen = set()

        while remainder%k != 0:
            n = remainder*10 + 1
            remainder = n % k
            length += 1
            if remainder in seen:
                return -1
            else:
                seen.add(remainder)
        return length