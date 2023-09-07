from tkinter.messagebox import *
class BinaryToDecimal:
    def bin_dec(self,t):
        t=t.get()
        if '.' in t or ('2' in t or '3' in t or '4' in t or '5' in t or '6' in t or '7' in t or '8' in t or '9' in t):
            try:
               raise ValueError('incorrect value (point and number>1 not allowed)')
            except Exception as e:
               print('Error...',e)
               showerror('Error',e)
               return 'None'
        t=list(str(t))
        ans=0
        for i in range(len(t)):
            digit=t.pop()
            if digit == '1':
                ans=ans+ pow(2,i)
        if ans!= 0:
            return ans
        else:
            return 'None'

class DecimalToBinary:
    def dec_bin (self,t):
        try:
            t=int(t.get())
            b=''
            while t!= 0:
                b= b+str(t%2)
                t=t//2
            ans=''
            for i in range(len(b)-1,-1,-1):
                ans+=b[i]
            return ans
        except Exception as e:
            print('Error...',e)
            showerror('Error',e)
            return 'None'
        
           


