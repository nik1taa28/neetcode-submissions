class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        sub=[]
        def comb(i,target):
            if target==0:
                res.append(sub.copy())
                return
            if target<0 or i>=len(nums):
                return

            sub.append(nums[i])
            comb(i,target-nums[i])

            sub.pop()
            comb(i+1,target)

        comb(0,target)
        return res
            
