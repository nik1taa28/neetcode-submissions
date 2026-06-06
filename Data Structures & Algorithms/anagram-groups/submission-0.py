class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        for i in strs:
            word="".join(sorted(i))
            if word in dict:
                dict[word].append(i)
            else:
                dict[word]=[i]
        return list(dict.values())
        
        