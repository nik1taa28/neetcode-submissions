class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num = {}
        for i,n in enumerate(nums):
            complement = target-n
            if complement in num:
                return [num[complement],i] 
            num[n]=i
        