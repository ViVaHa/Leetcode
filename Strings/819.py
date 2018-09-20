class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        if len(paragraph)==0:
            return ""
        start=0
        word=""
        d={}
        for i in range(len(paragraph)):
            if (ord(paragraph[i])<=91 and ord(paragraph[i])>=65) or (ord(paragraph[i])<=123 and ord(paragraph[i])>=97):
                word+=paragraph[i]
            else:
                if word.lower() not in banned and word!="":
                    word=word.lower()
                    if word in d:
                        d[word]+=1
                    else:
                        d[word]=1
                word=""
        if word not in banned and word!="":
                    word=word.lower()
                    if word in d:
                        d[word]+=1
                    else:
                        d[word]=1
        #print(d)
        import operator
        return max(d.items(), key=operator.itemgetter(1))[0]
        
