class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if not stack and s[i].isalpha():
                stack.append(s[i])
            elif s[i].isdigit() and stack:
                stack.pop()
            elif s[i].isalpha():
                stack.append(s[i])
        return "".join(stack)