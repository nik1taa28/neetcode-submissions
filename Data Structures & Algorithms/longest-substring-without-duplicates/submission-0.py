class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,right=0,0
        c=set()
        length=0
        while right < len(s):
            while s[right] in c:      
                c.remove(s[left])
                left += 1
            c.add(s[right])            
            length = max(length, right - left + 1) 
            right += 1
        return length