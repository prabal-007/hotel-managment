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

minifrm1 = Frame(mainfrm,relief=SUNKEN,border=5)

# frame for Vegetarial items - minifrm1

f1 = Frame(minifrm1)
Label(f1,text='VEGETARIAN', bg='orange',font='arial 8 bold').pack(pady=2,fill=X)
radio =Radiobutton(f1,text='Roti', variable=staVar, value='Roti',padx='5').pack(padx=5,side=LEFT)
lenVer1 = Spinbox(f1, from_=3, to_=23, width=5, relief=SUNKEN)
lenVer1.pack(side=LEFT,padx=10)
rvar = IntVar()
Entry(f1,textvariable=rvar,font='10',width='4').pack()
f1.pack(padx=5,pady=2)
f2 = Frame(minifrm1)
radio =Radiobutton(f2,text='Roti', variable=staVar, value='Roti',padx='5').pack(padx=5,side=LEFT)
lenVer2 = Spinbox(f2, from_=3, to_=23, width=5, relief=SUNKEN)
lenVer2.pack(side=LEFT,padx=5)
rvar = IntVar()
Entry(f2,textvariable=rvar,font='10',width='4').pack()
f2.pack(padx=5,pady=2)
f3 = Frame(minifrm1)
radio =Radiobutton(f3,text='Roti', variable=staVar, value='Roti',padx='5').pack(padx=5,side=LEFT)
lenVer1 = Spinbox(f3, from_=3, to_=23, width=5, relief=SUNKEN)
lenVer1.pack(side=LEFT,padx=10)
rvar = IntVar()
Entry(f3,textvariable=rvar,font='10',width='4').pack()
f3.pack(padx=5,pady=2)
f4 = Frame(minifrm1)
radio =Radiobutton(f4,text='Roti', variable=staVar, value='Roti',padx='5').pack(padx=5,side=LEFT)
lenVer2 = Spinbox(f4, from_=3, to_=23, width=5, relief=SUNKEN)
lenVer2.pack(side=LEFT,padx=5)
rvar = IntVar()
Entry(f4,textvariable=rvar,font='10',width='4').pack()
f4.pack(padx=5,pady=2)
f5 = Frame(minifrm1)
radio =Radiobutton(f5,text='Roti', variable=staVar, value='Roti',padx='5').pack(padx=5,side=LEFT)
lenVer1 = Spinbox(f5, from_=3, to_=23, width=5, relief=SUNKEN)
lenVer1.pack(side=LEFT,padx=10)
rvar = IntVar()
Entry(f5,textvariable=rvar,font='10',width='4').pack()
f5.pack(padx=5,pady=2)
f6 = Frame(minifrm1)
radio =Radiobutton(f6,text='Roti', variable=staVar, value='Roti',padx='5').pack(padx=5,side=LEFT)
lenVer2 = Spinbox(f6, from_=3, to_=23, width=5, relief=SUNKEN)
lenVer2.pack(side=LEFT,padx=5)
Entry(f6,textvariable=rvar,font='10',width='4').pack()
f6.pack(padx=5,pady=2)
f7 = Frame(minifrm1)
radio =Radiobutton(f7,text='Roti', variable=staVar, value='Roti',padx='5').pack(padx=5,side=LEFT)
lenVer2 = Spinbox(f7, from_=3, to_=23, width=5, relief=SUNKEN)
lenVer2.pack(side=LEFT,padx=5)
Entry(f7,textvariable=rvar,font='10',width='4').pack()
f7.pack(padx=5,pady=2)
f8 = Frame(minifrm1)
radio =Radiobutton(f8,text='Roti', variable=staVar, value='Roti',padx='5').pack(padx=5,side=LEFT)
lenVer1 = Spinbox(f8, from_=3, to_=23, width=5, relief=SUNKEN)
lenVer1.pack(side=LEFT,padx=10)
Entry(f8,textvariable=rvar,font='10',width='4').pack()
f8.pack(padx=5,pady=2)
f9 = Frame(minifrm1)
radio =Radiobutton(f9,text='Roti', variable=staVar, value='Roti',padx='5').pack(padx=5,side=LEFT)
lenVer2 = Spinbox(f9, from_=3, to_=23, width=5, relief=SUNKEN)
lenVer2.pack(side=LEFT,padx=5)
Entry(f9,textvariable=rvar,font='10',width='4').pack()
f9.pack(padx=5,pady=2)
f10 = Frame(minifrm1)
radio =Radiobutton(f10,text='Roti', variable=staVar, value='Roti',padx='5').pack(padx=5,side=LEFT)
lenVer1 = Spinbox(f10, from_=3, to_=23, width=5, relief=SUNKEN)
lenVer1.pack(side=LEFT,padx=10)
Entry(f10,textvariable=rvar,font='10',width='4').pack()
f10.pack(padx=5,pady=2)
f11 = Frame(minifrm1)
radio =Radiobutton(f11,text='Roti', variable=staVar, value='Roti',padx='5').pack(padx=5,side=LEFT)
lenVer2 = Spinbox(f11, from_=3, to_=23, width=5, relief=SUNKEN)
lenVer2.pack(side=LEFT,padx=5)
Entry(f11,textvariable=rvar,font='10',width='4').pack()
f11.pack(padx=5,pady=2)
f12 = Frame(minifrm1)
radio =Radiobutton(f12,text='Roti', variable=staVar, value='Roti',padx='5').pack(padx=5,side=LEFT)
lenVer1 = Spinbox(f12, from_=3, to_=23, width=5, relief=SUNKEN)
lenVer1.pack(side=LEFT,padx=10)
Entry(f12,textvariable=rvar,font='10',width='4').pack()
f12.pack(padx=5,pady=2)
f13 = Frame(minifrm1)
radio =Radiobutton(f13,text='Roti', variable=staVar, value='Roti',padx='5').pack(padx=5,side=LEFT)
lenVer2 = Spinbox(f13, from_=3, to_=23, width=5, relief=SUNKEN)
lenVer2.pack(side=LEFT,padx=5)
Entry(f13,textvariable=rvar,font='10',width='4').pack()
f13.pack(padx=5,pady=2)
f14 = Frame(minifrm1)
radio =Radiobutton(f14,text='Roti', variable=staVar, value='Roti',padx='5').pack(padx=5,side=LEFT)
lenVer1 = Spinbox(f14, from_=3, to_=23, width=5, relief=SUNKEN)
lenVer1.pack(side=LEFT,padx=10)
Entry(f14,textvariable=rvar,font='10',width='4').pack()
f14.pack(padx=5,pady=2)
f15 = Frame(minifrm1)
radio =Radiobutton(f15,text='Roti', variable=staVar, value='Roti',padx='5').pack(padx=5,side=LEFT)
lenVer2 = Spinbox(f15, from_=3, to_=23, width=5, relief=SUNKEN)
lenVer2.pack(side=LEFT,padx=5)
Entry(f15,textvariable=rvar,font='10',width='4').pack()
f15.pack(padx=5,pady=2)
minifrm1.pack(side=LEFT,padx=5,pady=5,fill=Y)   

                    # frame for Indian breads column - minifrm2

minifrm2 = Frame(mainfrm,relief=SUNKEN,border='5')
f1 = Frame(minifrm2)
Label(f1,text='Indian Breads', bg='orange',font='arial 8 bold').pack(fill=X,pady=2)
radio =Radiobutton(f1,text='Roti', variable=staVar, value='Roti',padx='5').pack(padx=5,side=LEFT)
lenVer1 = Spinbox(f1, from_=3, to_=23, width=5, relief=SUNKEN)
lenVer1.pack(side=LEFT,padx=10)
Entry(f1,textvariable=rvar,font='10',width='4').pack()
f1.pack(padx=5,pady=2)
f2 = Frame(minifrm2)
radio =Radiobutton(f2,text='Roti', variable=staVar, value='Roti',padx='5').pack(padx=5,side=LEFT)
lenVer2 = Spinbox(f2, from_=3, to_=23, width=5, relief=SUNKEN)
lenVer2.pack(side=LEFT,padx=5)
Entry(f2,textvariable=rvar,font='10',width='4').pack()
f2.pack(padx=5,pady=2)
f3 = Frame(minifrm2)
radio =Radiobutton(f3,text='Roti', variable=staVar, value='Roti',padx='5').pack(padx=5,side=LEFT)
lenVer1 = Spinbox(f3, from_=3, to_=23, width=5, relief=SUNKEN)
lenVer1.pack(side=LEFT,padx=10)
Entry(f3,textvariable=rvar,font='10',width='4').pack()
f3.pack(padx=5,pady=2)
f4 = Frame(minifrm2)
radio =Radiobutton(f4,text='Roti', variable=staVar, value='Roti',padx='5').pack(padx=5,side=LEFT)
lenVer2 = Spinbox(f4, from_=3, to_=23, width=5, relief=SUNKEN)
lenVer2.pack(side=LEFT,padx=5)
Entry(f4,textvariable=rvar,font='10',width='4').pack()
f4.pack(padx=5,pady=2)
f5 = Frame(minifrm2)
radio =Radiobutton(f5,text='Roti', variable=staVar, value='Roti',padx='5').pack(padx=5,side=LEFT)
lenVer1 = Spinbox(f5, from_=3, to_=23, width=5, relief=SUNKEN)
lenVer1.pack(side=LEFT,padx=10)
Entry(f5,textvariable=rvar,font='10',width='4').pack()
f5.pack(padx=5,pady=2)
f6 = Frame(minifrm2)
radio =Radiobutton(f6,text='Roti', variable=staVar, value='Roti',padx='5').pack(padx=5,side=LEFT)
lenVer2 = Spinbox(f6, from_=3, to_=23, width=5, relief=SUNKEN)
lenVer2.pack(side=LEFT,padx=5)
Entry(f1,textvariable=rvar,font='10',width='4').pack()
f6.pack(padx=5,pady=2)
f7 = Frame(minifrm2)
Label(f7,text='Tava Special', fg='Green',font='arial 8 bold').pack(fill=X,pady=2)
radio =Radiobutton(f7,text='Roti', variable=staVar, value='Roti',padx='5').pack(padx=5,side=LEFT)
lenVer1 = Spinbox(f7, from_=3, to_=23, width=5, relief=SUNKEN)
lenVer1.pack(side=LEFT,padx=10)
Entry(f7,textvariable=rvar,font='10',width='4').pack()
f7.pack(padx=5,pady=2)
f8 = Frame(minifrm2)
radio =Radiobutton(f8,text='Roti', variable=staVar, value='Roti',padx='5').pack(padx=5,side=LEFT)
lenVer2 = Spinbox(f8, from_=3, to_=23, width=5, relief=SUNKEN)
lenVer2.pack(side=LEFT,padx=5)
Entry(f8,textvariable=rvar,font='10',width='4').pack()
f8.pack(padx=5,pady=2)
f9 = Frame(minifrm2)
radio =Radiobutton(f9,text='Roti', variable=staVar, value='Roti',padx='5').pack(padx=5,side=LEFT)
lenVer1 = Spinbox(f9, from_=3, to_=23, width=5, relief=SUNKEN)
lenVer1.pack(side=LEFT,padx=10)
Entry(f9,textvariable=rvar,font='10',width='4').pack()
f9.pack(padx=5,pady=2)
f10 = Frame(minifrm2)
radio =Radiobutton(f10,text='Roti', variable=staVar, value='Roti',padx='5').pack(padx=5,side=LEFT)
lenVer2 = Spinbox(f10, from_=3, to_=23, width=5, relief=SUNKEN)
lenVer2.pack(side=LEFT,padx=5)
Entry(f10,textvariable=rvar,font='10',width='4').pack()
f10.pack(padx=5,pady=2)
f11 = Frame(minifrm2)
radio =Radiobutton(f11,text='Roti', variable=staVar, value='Roti',padx='5').pack(padx=5,side=LEFT)
lenVer1 = Spinbox(f11, from_=3, to_=23, width=5, relief=SUNKEN)
lenVer1.pack(side=LEFT,padx=10)
Entry(f11,textvariable=rvar,font='10',width='4').pack()
f11.pack(padx=5,pady=2)
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
