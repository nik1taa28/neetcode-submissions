class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []   
        res=[]
        path=[]
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
        def back(i):
            if i==len(digits):
                res.append("".join(path))
                return

            for letter in digtochar[digits[i]]:
                path.append(letter)
                back(i+1)
                path.pop()

        back(0)
        return res