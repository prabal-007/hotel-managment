from tkinter import *

root = Tk()
root.title('Hotel Management')
root.geometry('1030x800')
root.configure(background='Gold')
frm1 = Frame(bg='red')
Label(frm1,text='Hotel Management SYSTEM', font='arial 25 bold', padx='15', pady='5', bg='gold', relief=SUNKEN, border=4).pack(padx=10, pady=10, fill=X)
frm1.pack(side=TOP, fill=X)
staVar=StringVar()
# ////////////////////////////////////////////////// ///////////////////
def submitOrder():
    screen.configure(state=NORMAL)
    screen.delete('1.0', END)
    screen.insert(END,f'Item\tQty\tPrice\n\n')
    result = zip(vegItems,breads)
    for i in set(result):
        screen.insert(END,f'{i}\n')
    screen.configure(state=DISABLED)
    
rightfrm = Frame(root,bg='gold')
mainfrm = Frame(rightfrm,relief=SUNKEN, border='8',background='red')
Label(mainfrm,text='MENU',font='arial 20 bold',padx='5').pack()
# staVar=StringVar()
# staVar.set('Roti')

# frame for Vegetarial items - minifrm1
vegItems = {'Roti':1,'Daal':2,'Paneer':2,'Gobi aloo':3,'Palak Paneer':4,'Rajma':5,'mutter paneer':6,'Kaali daal':3,
'Chole':7,'Daal-Palak':6,'Broccoli Paneer':8,'Pinto Posole':9,'Crispy Baked':4,'Seaweeds':6,'Nuts.Paneer':7,'Leafy Greens':2}
breads = ['Roti','Daal','Paneer','Gobi aloo','Roti','Daal','Paneer','Gobi aloo','Roti','Daal','Paneer aloo']
southIndian = ['Roti','Daal','Paneer','Gobi aloo','Roti','Daal','Paneer','Gobi aloo','Roti','Daal']
frames = ['f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11','f12','f13','f14','f15','f16']
veg_vars = []
breads_vars = []
southIndian_vars = []
for val in range(50):
    val = StringVar()
    veg_vars.append(val)
for val in range(50):
    val = StringVar()
    breads_vars.append(val)
for val in range(50):
    val = StringVar()
    southIndian_vars.append(val)

minifrm1 = Frame(mainfrm,relief=SUNKEN,border=5)
count = 0
var_i=0

for item, price in vegItems.items():
    frames[count] = Frame(minifrm1)
    if count == 0:
        Label(frames[count],text='VEGETARIAN',  bg='orange',font='arial 8 bold').pack(pady=2,fill=X)
    radio =Checkbutton(frames[count],text=item, variable=veg_vars[var_i],padx='5')
    radio.pack(padx=5,side=LEFT)
    radio.deselect()
    lenVer1 = Spinbox(frames[count], from_=0, to_=23, width=5, relief=SUNKEN)
    lenVer1.pack(side=LEFT,padx=10)
    rvar = IntVar()
    rvar.set(f'{price}')
    Entry(frames[count],textvariable=rvar,font='10',width='4').pack()
    frames[count].pack(padx=5,pady=2)
    count += 1
    var_i += 1
minifrm1.pack(side=LEFT,padx=5,pady=5,fill=Y)   

                   # frame for Indian breads column - minifrm2
minifrm2 = Frame(mainfrm,relief=SUNKEN,border='5')
count = 0
for item in breads:
    frames[count] = Frame(minifrm2)
    if count == 0:
        Label(frames[count],text='Indian Breads',  bg='orange',font='arial 8 bold').pack(pady=2,fill=X)
    if count == 6:
        Label(frames[count],text='Tava Special',  fg='Green',font='arial 8 bold').pack(pady=2,fill=X)
    radio =Checkbutton(frames[count],text=item, variable=breads_vars[var_i], padx='5')
    radio.pack(padx=5,side=LEFT)
    radio.deselect()
    lenVer1 = Spinbox(frames[count], from_=0, to_=23, width=5, relief=SUNKEN)
    lenVer1.pack(side=LEFT,padx=10)
    rvar = IntVar()
    Entry(frames[count],textvariable=rvar,font='10',width='4').pack()
    frames[count].pack(padx=5,pady=2)
    count += 1
    var_i += 1
minifrm2.pack(padx=5,pady=5,anchor='n',side=LEFT)

minifrm3 = Frame(mainfrm,relief=SUNKEN,border='5')
count = 0
for item in southIndian:
    frames[count] = Frame(minifrm3)
    if count == 0:
        Label(frames[count],text='South Indian',  bg='orange',font='arial 8 bold').pack(pady=2,fill=X)
    if count == 6:
        Label(frames[count],text='Rice',  bg='Orange',font='arial 8 bold').pack(pady=2,fill=X)
    radio = Checkbutton(frames[count],text=item, variable=southIndian_vars[var_i], padx='5')
    radio.pack(padx=5,side=LEFT)
    radio.deselect()
    lenVer1 = Spinbox(frames[count], from_=0, to_=23, width=5, relief=SUNKEN)
    lenVer1.pack(side=LEFT,padx=10)
    rvar = IntVar()
    Entry(frames[count],textvariable=rvar,font='10',width='4').pack()
    frames[count].pack(padx=5,pady=2)
    count += 1
    var_i += 1
minifrm3.pack(padx=5,pady=5,anchor='e')

mainfrm.pack(pady=2,padx=1)
    # //////////////////////////////////////////////////////////////////////////

bottomfrm = Frame(rightfrm,relief=FLAT, border='8',background='red')
Button(bottomfrm,text='BACK', font='arial 15 bold',relief=SUNKEN, command=NONE).pack(padx=10,side=LEFT)
submit = Button(bottomfrm,text='SUBMIT ORDER', font='arial 15 bold',relief=SUNKEN, command=submitOrder).pack(padx=10,side=RIGHT)
Button(bottomfrm,text='RESET', font='arial 15 bold',relief=SUNKEN, command=NONE).pack(padx=10,side=RIGHT)
bottomfrm.pack(side=BOTTOM)
rightfrm.pack(fill=X,side=LEFT,anchor='n')
    # ///////////////////////////////////////////////////////////////////////////
    
sidefrm = Frame(root,bg='red')
Label(sidefrm,text='Order Details', font='arial 15 bold',width=8,padx=5).pack(padx=5,fill=X)
var = StringVar()
scroll = Scrollbar(sidefrm)
scroll.pack(fill=Y,side=RIGHT,pady=10)
var.set('Item  Qty  Price\n ')

screen = Text(sidefrm,font='lucida 14 bold', yscrollcommand=scroll.set)
screen.pack(fill=Y,expand=TRUE, padx=5, pady='10')
screen.insert(END,f'\n\n\tPress\n      \'SUBMIT ORDER\'\n     to get order your\n            summery')
screen.configure(state=DISABLED)
scroll.config(command=screen.yview)
payfrm = Frame(sidefrm,relief=FLAT, border='8',background='red')
Button(payfrm,text='Pay Now', font='arial 15 bold',relief=SUNKEN, command=NONE,padx=5).pack(padx=10,pady=5)
Button(payfrm,text='Add More', font='arial 10 bold',relief=SUNKEN, command=NONE).pack(padx=10,pady=5)
payfrm.pack(side=BOTTOM)

sidefrm.pack(pady=2,padx=1,side=RIGHT,anchor='n')
value = staVar.get()
print(value)

root.mainloop()
