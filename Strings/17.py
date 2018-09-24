class Solution(object):
    def backTrack(self,digits,index,kvmap,temp,ans):
        if index==len(digits):
            ans.append(temp)
            return
        items=kvmap[digits[index]]
        for item in items:
            self.backTrack(digits,index+1,kvmap,temp+item,ans)
            
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits)==0:
            return []
        kvmap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        ans=[]
        temp=""
        self.backTrack(digits,0,kvmap,temp,ans)
        return ans
        
