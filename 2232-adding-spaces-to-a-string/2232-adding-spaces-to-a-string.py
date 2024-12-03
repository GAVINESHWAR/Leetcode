class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ""
        c = 0
        for i in range(len(s)):
            if c<len(spaces) and i == spaces[c]:
                ans =ans + " " + s[i]
                c+=1
            else:
                ans+=s[i]
        return ans
        