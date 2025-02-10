class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        dic = {"a":"a","e":"e","i":"i","o":"o","u":"u"}
        sliding = list(s[:k])
        count =0
        for i in sliding:
            if i in dic:
                count += 1
        ans = count
        for i in range(len(s)-k):
            if s[i] in dic:
                count -= 1
            if s[i+k] in dic:
                count+=1
            ans = max(ans, count)
        return ans