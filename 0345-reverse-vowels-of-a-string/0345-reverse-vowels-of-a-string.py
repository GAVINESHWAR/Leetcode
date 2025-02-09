class Solution:
    def reverseVowels(self, s: str) -> str:
        dic = {"A":"A","I":"I","E":"E","O":"O","U":"U","a":"a","e":"e","i":"i","o":"o","u":"u"}
        i = 0
        j = len(s)-1
        dummy = list(s)
        while i<=j:
            if s[i] in dic and s[j] in dic:
                dummy[i], dummy[j] = dummy[j], dummy[i]
                i+=1
                j-=1
            elif s[i] in dic and s[j] not in dic:
                j-=1
            elif s[i] not in dic and s[j] in dic:
                i+=1
            elif s[i] not in dic and s[j] not in dic:
                j-=1
        return "".join(dummy)
