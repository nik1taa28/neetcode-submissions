class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num=sorted(nums)
        res=[]
        for i in range(len(num)):
            if i>0 and num[i]==num[i-1]:
                continue
            l,r=i+1,len(num)-1
            while l<r:
                if(num[i]+num[l]+num[r]<0):
                    l+=1
                elif(num[i]+num[l]+num[r]>0):
                    r-=1
                else:
                    res.append([num[i], num[l],num[r]])
                    l+=1
                    r-=1
                    while l<r and num[l]==num[l-1]:
                        l+=1
                    while l<r and num[r]==num[r+1]:
                        r-=1
        return res
        
            