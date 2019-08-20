from tkinter import *

window = Tk()

l1 = Label(window,text = "Row Current Ind")
l1.grid(row=1,column=0)

l2 = Label(window,text = "Row Deleted Ind")
l2.grid(row=1,column=2)

l3 = Label(window,text = "Region")
l3.grid(row=1,column=4)

l4 = Label(window,text = "CPT Codes")
l4.grid(row=2,column=0)

l5 = Label(window,text = "Valid From")
l5.grid(row=2,column=2)

l6 = Label(window,text = "Valid To")
l6.grid(row=2,column=4)

l7 = Label(window,text = "Key Value")
l7.grid(row=3,column=0)

Row_Current=StringVar()
e1=Entry(window,textvariable=Row_Current)
e1.grid(row=1,column=1)

Row_Deleted=StringVar()
e2=Entry(window,textvariable=Row_Deleted)
e2.grid(row=1,column=3)

Region_char=StringVar()
e3=Entry(window,textvariable=Region_char)
e3.grid(row=1,column=5)

CPT_char=StringVar()
e4=Entry(window,textvariable=CPT_char)
e4.grid(row=2,column=1)

Valid_From=StringVar()
e5=Entry(window,textvariable=Valid_From)
e5.grid(row=2,column=3)

Valid_To=StringVar()
e6=Entry(window,textvariable=Valid_To)
e6.grid(row=2,column=5)

Key_Value=IntVar()
e6=Entry(window,textvariable=Key_Value)
e6.grid(row=3,column=1)

list1=Listbox(window, height = 15, width = 135)
list1.grid(row=4,column=0,rowspan =6, columnspan=4)

sb1 = Scrollbar(window)
sb1.grid(row =4,column =4,rowspan = 6)

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command=list1.yview)

b1=Button(window,text="View All", width=12)
b1.grid(row=4,column = 5)

b2=Button(window,text="Search Entry", width=12)
b2.grid(row=5,column = 5)

b3=Button(window,text="Add Entry", width=12)
b3.grid(row=6,column = 5)

b4=Button(window,text="Update Selected", width=12)
b4.grid(row=7,column = 5)

b4=Button(window,text="Delete Selected", width=12)
b4.grid(row=8,column = 5)


window.mainloop()