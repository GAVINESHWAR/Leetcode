class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        ans = []
        if k==0:
            ans = [0]*len(code)
        elif k>0:
            for i in range(len(code)):
                sum1 = 0
                for j in range(abs(k)):
                    sum1+=code[(i+j+1)%len(code)]
                ans.append(sum1)
        elif k<0:
            for i in range(len(code)):
                sum1 = 0
                for j in range(abs(k)):
                    sum1+=code[(i-j-1)%len(code)]
                ans.append(sum1)
        return ans

