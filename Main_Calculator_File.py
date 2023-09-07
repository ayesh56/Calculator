# In python shell run time errorand already runloop started  show due to threading but GUI work perfect.
from tkinter import *
from tkinter.messagebox import *
from audio_file import playaudio
import threading
# ***AS per design constraint  requirement use inheritance
class Calculator(Tk):
    def __init__ (self):
        super().__init__()
        Font=('verdanna',25,'bold')
        self.geometry('510x660')
        self.title('MY CALCULATOR')

        # picture label
        pic= PhotoImage(file="img.png")
        pic=pic.subsample(6,6)
        picturelabel=Label(self,image=pic)
        picturelabel.pack(side=TOP,pady=5)

        #Heading label
        headinglabel=Label(self,text='My Calculator',font=Font,fg='blue')
        headinglabel.pack(side=TOP)

        # Text field
        textfield= Entry(self,font=Font,fg='pink',justify=CENTER)
        textfield.pack(side=TOP,pady=10,fill=X,padx=10)

        # instantiate the object of class Num_Button
        # ***AS per design constraint requirement use composition 
        B=Num_Button(self,textfield)

        self.mainloop()

# Button class
class Num_Button(Frame):
    def __init__ (self,r,t):
        super().__init__(r)
        Font=('verdanna',25,'bold')

        #import CONVERT file

        from CONVERT_FILE import BinaryToDecimal,DecimalToBinary 

        # Making child class for classes in CONVERT file through multiple inheritance
        # ***As per design constraint requirement use multiple inheritance and method overriding

        class child_BD (BinaryToDecimal,DecimalToBinary):
            def __init__(self,t):
                self.t=t

            # initialize the object of class playaudio in audio_file and i instantiate object outside the init method of
            #child_BD because it access from other functions of Num_Button class such as clear,all_clear and click_btn_function
            #and due to this reason instantiate outside and also in bin_dec and dec_bin method because it can't access from
            #here.
            self.ob=playaudio()
            
            def bin_dec(self):
                ans=super().bin_dec(self.t)
                if ans!='None':
                    self.t.delete(0,END)
                    self.t.insert(0,ans)
                    print('binary to decimal')
                    print(ans)
                    ob=playaudio()
                    tr=threading.Thread(target=ob.speak,args=('Bin To Dec',))
                    tr.start()
                    return
                else:
                    self.t.delete(0,END)
                    return
            def dec_bin(self):
                ans=super().dec_bin(self.t)
                if ans!='None':
                    self.t.delete(0,END)
                    self.t.insert(0,ans)
                    print('decimal to binary')
                    print(ans)
                    ob=playaudio()
                    tr=threading.Thread(target=ob.speak,args=('Dec To Bin',))
                    tr.start()
                    return
                else:
                    self.t.delete(0,END)
                    return
       # initialize the object of child_BD 
       
        Ch=child_BD(t)

       # important function

        def clear():
            ex=t.get()
            ex=ex[0:len(ex)-1]
            t.delete(0,END)
            t.insert(0,ex)
            tr=threading.Thread(target=self.ob.speak,args=('<--',))
            tr.start()
            return
        
        def all_clear():
            t.delete(0,END)
            tr=threading.Thread(target=self.ob.speak,args=('AC',))
            tr.start()
            return
            
            
        def click_btn_function(event):
            print('btn clicked')
            b=event.widget
            text=b['text']
            print(text)
            tr=threading.Thread(target=self.ob.speak,args=(text,))
            tr.start()
            if text=='x':
                t.insert(END,'*')
                return
            # *** As per design constraint requirement use exception handling
            if text=='=':
                try:
                    ex=t.get()
                    answer=eval(ex)
                    t.delete(0,END)
                    t.insert(0,answer)
                    print(answer)
                except Exception as e:
                    print('Error...',e)
                    showerror('Error',e)
                    t.delete(0,END)                          
                return
            t.insert(END,text)
            return
        

        # Adding button
        count=1
        for i in range(0,3):
            for j in range(0,3):
                Btn=Button(self,text=str(count),font=Font,relief="raised",width=5,fg='blue',bg='pink',activeforeground='white',
                           activebackground='skyblue')
                Btn.grid(row=i,column=j,padx=3,pady=3)
                count+=1
                Btn.bind('<Button-1>',click_btn_function)
                


        ZeroBtn=Button(self,text='0',font=Font,relief="raised",width=5,fg='blue',bg='pink',activeforeground='white',
                           activebackground='skyblue')
        ZeroBtn.grid(row=3,column=0,padx=3,pady=3)


        DotBtn=Button(self,text='.',font=Font,relief="raised",width=5,fg='blue',bg='pink',activeforeground='white',
                           activebackground='skyblue')
        DotBtn.grid(row=3,column=1,padx=3,pady=3)


        EqualBtn=Button(self,text='=',font=Font,relief="raised",width=5,fg='blue',bg='pink',activeforeground='white',
                           activebackground='skyblue')
        EqualBtn.grid(row=3,column=2,padx=3,pady=3)


        PlusBtn=Button(self,text='+',font=Font,relief="raised",width=5,fg='blue',bg='pink',activeforeground='white',
                           activebackground='skyblue')
        PlusBtn.grid(row=0,column=3,padx=3,pady=3)


        MinusBtn=Button(self,text='-',font=Font,relief="raised",width=5,fg='blue',bg='pink',activeforeground='white',
                           activebackground='skyblue')
        MinusBtn.grid(row=1,column=3,padx=3,pady=3)


        MultiplyBtn=Button(self,text='x',font=Font,relief="raised",width=5,fg='blue',bg='pink',activeforeground='white',
                           activebackground='skyblue')
        MultiplyBtn.grid(row=2,column=3,padx=3,pady=3)

        DivideBtn=Button(self,text='/',font=Font,relief="raised",width=5,fg='blue',bg='pink',activeforeground='white',
                           activebackground='skyblue')
        DivideBtn.grid(row=3,column=3,padx=3,pady=3)

        ClearBtn=Button(self,text='<--',font=Font,relief="raised",width=11,fg='blue',bg='pink',activeforeground='white',
                           activebackground='skyblue',command=clear)
        ClearBtn.grid(row=4,column=0,columnspan=2,padx=3,pady=3)

        AllClearBtn=Button(self,text='AC',font=Font,relief="raised",width=11,fg='blue',bg='pink',activeforeground='white',
                           activebackground='skyblue',command=all_clear)
        AllClearBtn.grid(row=4,column=2,columnspan=2,padx=3,pady=3)

        Bin_Dec_Btn=Button(self,text='Bin To Dec',font=Font,relief="raised",width=11,fg='blue',bg='pink',activeforeground='white',
                           activebackground='skyblue',command=Ch.bin_dec)
        Bin_Dec_Btn.grid(row=5,column=0,columnspan=2,padx=3,pady=3)

        Dec_Bin_Btn=Button(self,text='Dec To Bin',font=Font,relief="raised",width=11,fg='blue',bg='pink',activeforeground='white',
                           activebackground='skyblue',command=Ch.dec_bin)
        Dec_Bin_Btn.grid(row=5,column=2,columnspan=2,padx=3,pady=3)

        # Binding all buttons

        PlusBtn.bind('<Button-1>',click_btn_function)
        MinusBtn.bind('<Button-1>',click_btn_function)
        MultiplyBtn.bind('<Button-1>',click_btn_function) 
        DivideBtn.bind('<Button-1>',click_btn_function)
        ZeroBtn.bind('<Button-1>',click_btn_function)
        DotBtn.bind('<Button-1>',click_btn_function) 
        EqualBtn.bind('<Button-1>',click_btn_function)
         
        self.pack(side=TOP,padx=10)

C=Calculator()
