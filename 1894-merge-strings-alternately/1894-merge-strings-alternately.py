class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        n1 = len(word1)
        n2 = len(word2)
        i = 0
        j = 0
        while i<n1 and j<n2:
            ans += word1[i]
            ans += word2[j]
            i+=1
            j+=1
        while i<n1:
            ans+= word1[i:]
            i=n1
        while j<n2:
            ans += word2[j:] 
            j=n2
        return ans       