class Solution:
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        num1=a.split("+")
        num2=b.split("+")
        num1_real=num1[0]
        num1_imag=num1[1][0:len(num1[1])-1]
        num2_real=num2[0]
        num2_imag=num2[1][0:len(num2[1])-1]
        if num2_imag[0]=='-':
            num2_imag=-1*(int(num2_imag[1:]))
        else:
            num2_imag=int(num2_imag)
        if num1_imag[0]=='-':
            num1_imag=-1*(int(num1_imag[1:]))
        else:
            num1_imag=int(num1_imag)
        if num1_real[0]=='-':
            num1_real=-1*(int(num1_real[1:]))
        else:
            num1_real=int(num1_real)
        if num2_real[0]=='-':
            num2_real=-1*(int(num2_real[1:]))
        else:
            num2_real=int(num2_real)
        
        ans_real=(num1_real*(num2_real))-(((num1_imag)*(num2_imag)))
        ans_imag = ((num1_real)*(num2_imag)) + ((num2_real)*(num1_imag))
        return str(ans_real)+ "+" +str(ans_imag)+"i"
                  
        
        
