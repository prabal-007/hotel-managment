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

breads = ['Roti','Daal','Paneer','Gobi aloo','Roti','Daal','Paneer','Gobi aloo','Roti','Daal','Paneer']
frames = ['f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11']

minifrm2 = Frame(mainfrm,relief=SUNKEN,border='5')

count = 0
for item in breads:
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


southIndian = ['Roti','Daal','Paneer','Gobi aloo','Roti','Daal','Paneer','Gobi aloo','Roti','Daal']
frames = ['f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11']

minifrm3 = Frame(mainfrm,relief=SUNKEN,border='5')
count = 0
for item in southIndian:
    frames[count] = Frame(minifrm3)
    if count == 0:
        Label(frames[count],text='South Indian',  bg='orange',font='arial 8 bold').pack(pady=2,fill=X)
    if count == 6:
        Label(frames[count],text='Rice',  bg='Orange',font='arial 8 bold').pack(pady=2,fill=X)
    radio =Radiobutton(frames[count],text=item, variable=staVar, value=item,padx='5').pack(padx=5,side=LEFT)
    lenVer1 = Spinbox(frames[count], from_=0, to_=23, width=5, relief=SUNKEN)
    lenVer1.pack(side=LEFT,padx=10)
    rvar = IntVar()
    Entry(frames[count],textvariable=rvar,font='10',width='4').pack()
    frames[count].pack(padx=5,pady=2)
    count += 1

minifrm3.pack(padx=5,pady=5,anchor='e')

mainfrm.pack(pady=2,padx=1,fill=X,side=LEFT)
root.mainloop()
