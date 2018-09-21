class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars)==0:
            return 0
        index=0
        count=1
        i=0
        curr=chars[0]
        while i<len(chars)-1:
            if chars[i]!=chars[i+1]:
                if count>1:
                    chars[index]=curr
                    index+=1
                    count=str(count)
                    for j in range(len(count)):
                        chars[index]=count[j]
                        index+=1
                        j+=1
                else:
                    chars[index]=curr
                    index+=1
                
                count=1
                curr=chars[i+1]
            else:
                count+=1
            i+=1
        if count>1:
            chars[index]=curr
            index+=1
            count=str(count)
            for j in range(len(count)):
                chars[index]=count[j]
                index+=1
                j+=1
            return index
        else:
            chars[index]=curr
            return index+1
