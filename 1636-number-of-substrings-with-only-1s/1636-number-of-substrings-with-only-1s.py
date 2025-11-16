class Solution:
    def numSub(self, s: str) -> int:
        n = s.count("1")
        total = 0
        run = 0
        for cha in s:
            if cha == "1":
                run += 1
            else:
                total += run * (run + 1) // 2
                run = 0
        total += run * (run + 1) // 2
        return total %(pow(10,9)+7)
