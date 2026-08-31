class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        digtochar={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"qprs",
            "8":"tuv",
            "9":"wxyz"
        }
        def back(i,curStr):
            if len(curStr)==len(digits):
                res.append(curStr)
                return
            for c in digtochar[digits[i]]:
                back(i+1,curStr+c)
        if digits:
            back(0,"")

        return res