from tkinter import *

root = Tk()
root.title('Hotel Management')
root.geometry('700x600')
root.configure(background='red')
frm1 = Frame(bg='red')
Label(frm1,text='Hotel Management', font='arial 25 bold', padx='15', pady='5', bg='red', relief=SUNKEN, border=4).pack(padx=10, pady=10, fill=X)
frm1.pack(side=TOP, fill=X)

mainfrm = Frame(relief=SUNKEN, border='8',background='red')
staVar=StringVar()

# frame for Vegetarial items - minifrm1
vegItems = ['Roti','Daal','Paneer','Gobi aloo','Roti','Daal','Paneer','Gobi aloo','Roti','Daal','Paneer','Gobi aloo',
'Roti','Daal','Paneer','Gobi aloo']
frames = ['f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11','f12','f13','f14','f15','f16']

minifrm1 = Frame(mainfrm,relief=SUNKEN,border=5)

count = 0
for item in vegItems:
    frames[count] = Frame(minifrm1)
    if count == 0:
        Label(frames[count],text='VEGETARIAN',  bg='orange',font='arial 8 bold').pack(pady=2,fill=X)
    radio =Radiobutton(frames[count],text=item, variable=staVar, value=item,padx='5').pack(padx=5,side=LEFT)
    lenVer1 = Spinbox(frames[count], from_=0, to_=23, width=5, relief=SUNKEN)
    lenVer1.pack(side=LEFT,padx=10)
    rvar = IntVar()
    Entry(frames[count],textvariable=rvar,font='10',width='4').pack()
    frames[count].pack(padx=5,pady=2)
    count += 1

minifrm1.pack(side=LEFT,padx=5,pady=5,fill=Y)   

                    # frame for Indian breads column - minifrm2

vegItems = ['Roti','Daal','Paneer','Gobi aloo','Roti','Daal','Paneer','Gobi aloo','Roti','Daal','Paneer']
frames = ['f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11']

minifrm2 = Frame(mainfrm,relief=SUNKEN,border='5')

count = 0
for item in vegItems:
    frames[count] = Frame(minifrm2)
    if count == 0:
        Label(frames[count],text='Indian Breads',  bg='orange',font='arial 8 bold').pack(pady=2,fill=X)
    if count == 6:
        Label(frames[count],text='Tava Special',  fg='Green',font='arial 8 bold').pack(pady=2,fill=X)
    radio =Radiobutton(frames[count],text=item, variable=staVar, value=item,padx='5').pack(padx=5,side=LEFT)
    lenVer1 = Spinbox(frames[count], from_=0, to_=23, width=5, relief=SUNKEN)
    lenVer1.pack(side=LEFT,padx=10)
    rvar = IntVar()
    Entry(frames[count],textvariable=rvar,font='10',width='4').pack()
    frames[count].pack(padx=5,pady=2)
    count += 1
    
minifrm2.pack(padx=5,pady=5,anchor='n',side=LEFT)



minifrm3 = Frame(mainfrm,relief=SUNKEN,border='5')
f1 = Frame(minifrm3)
radio =Radiobutton(f1,text='Roti', variable=staVar, value='Roti',padx='5').pack(padx=5,side=LEFT)
lenVer1 = Spinbox(f1, from_=3, to_=23, width=5, relief=SUNKEN)
lenVer1.pack(side=LEFT,padx=10)
f1.pack(padx=5,pady=2)
f2 = Frame(minifrm3)
radio =Radiobutton(f2,text='Roti', variable=staVar, value='Roti',padx='5').pack(padx=5,side=LEFT)
lenVer2 = Spinbox(f2, from_=3, to_=23, width=5, relief=SUNKEN)
lenVer2.pack(side=LEFT,padx=5)
f2.pack(padx=5,pady=2)
f3 = Frame(minifrm3)
radio =Radiobutton(f3,text='Roti', variable=staVar, value='Roti',padx='5').pack(padx=5,side=LEFT)
lenVer1 = Spinbox(f3, from_=3, to_=23, width=5, relief=SUNKEN)
lenVer1.pack(side=LEFT,padx=10)
f3.pack(padx=5,pady=2)
f4 = Frame(minifrm3)
radio =Radiobutton(f4,text='Roti', variable=staVar, value='Roti',padx='5').pack(padx=5,side=LEFT)
lenVer2 = Spinbox(f4, from_=3, to_=23, width=5, relief=SUNKEN)
lenVer2.pack(side=LEFT,padx=5)
f4.pack(padx=5,pady=2)
f5 = Frame(minifrm3)
radio =Radiobutton(f5,text='Roti', variable=staVar, value='Roti',padx='5').pack(padx=5,side=LEFT)
lenVer1 = Spinbox(f5, from_=3, to_=23, width=5, relief=SUNKEN)
lenVer1.pack(side=LEFT,padx=10)
f5.pack(padx=5,pady=2)
f6 = Frame(minifrm3)
radio =Radiobutton(f6,text='Roti', variable=staVar, value='Roti',padx='5').pack(padx=5,side=LEFT)
lenVer2 = Spinbox(f6, from_=3, to_=23, width=5, relief=SUNKEN)
lenVer2.pack(side=LEFT,padx=5)
f6.pack(padx=5,pady=2)
minifrm3.pack(padx=5,pady=5,anchor='e')

mainfrm.pack(pady=2,padx=1,fill=X,side=LEFT)
root.mainloop()
