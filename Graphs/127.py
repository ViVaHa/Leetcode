class Solution:
    def differentByOneChar(self,word1,word2):
        count=0
        for i in range(len(word1)):
            if word1[i]!=word2[i]:
                count+=1
            if count>1:
                return False
        if count==1:
            return True
        return False
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if beginWord==endWord:
            return 0
        wordList=set(wordList)
        from collections import deque
        q=deque()
        q.append([beginWord,1])
        if beginWord in wordList:
            wordList.remove(beginWord)
        while len(q)>0:
            item=q.popleft()
            word=item[0]
            steps=item[1]
            if word==endWord:
                return steps
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    newWord=word[:i]+c+word[i+1:]
                    if newWord in wordList:
                        q.append([newWord,steps+1])
                        wordList.remove(newWord)
        return 0
        
