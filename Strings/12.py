class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        m = ["", "M", "MM", "MMM"]; 
        c = ["", "C", "CC", "CCC", "CD", "D",  
                        "DC", "DCC", "DCCC", "CM"]; 
        x = ["", "X", "XX", "XXX", "XL", "L",  
                        "LX", "LXX", "LXXX", "XC"]; 
        i = ["", "I", "II", "III", "IV", "V",  
                        "VI", "VII", "VIII", "IX"];
        thousands=m[int(num/1000)]
        hundreds=c[int((num%1000)/100)]
        tens=x[int((num%100)/10)]
        ones=i[int(num%10)]
        return thousands+hundreds+tens+ones
