class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        dummy = s.split(" ")
        dummy = list(dummy)
        n = len(dummy)
        for i in range(n//2):
            dummy[i], dummy[n-i-1] = dummy[n-i-1], dummy[i]
        ans = ""
        for i in range(n):
            if dummy[i]!="":
                ans += dummy[i] + " "  
        return ans.strip()