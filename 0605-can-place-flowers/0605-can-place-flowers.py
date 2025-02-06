class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        for i in range(length):
            if i==0 and length>1 and flowerbed[i+1]!=1 and flowerbed[i]==0:
                n-=1
                flowerbed[i]=1
            elif i>0 and i<length-1 and flowerbed[i]==0 and flowerbed[i+1]==0 and flowerbed[i-1]==0:
                n-=1
                flowerbed[i]=1
            elif i==length-1 and flowerbed[i]==0 and flowerbed[i-1]==0:
                n-=1
                flowerbed[i]=1
        if n<=0:
            return True
        else:
            return False
