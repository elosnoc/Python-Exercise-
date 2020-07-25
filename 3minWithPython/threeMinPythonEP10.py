from tkinter import *
from tkinter import ttk
GUI = Tk()
GUI.geometry('500x300')



B1 = ttk.Button(GUI,text='Hello')
B1.place(x=100,y=100)
B2 = ttk.Button(GUI,text='Hi')
B2.place(x=200,y=100)


L1 = ttk.Label(GUI,text='Text is here')
L1.pack()


result = StringVar()
L2 = ttk.Label(GUI,textvariable=result)

L2.pack(pady=20)
result.set('-------------')

def Hello():
    result.set('Hello')
def Hi():
    result.set('Hi')

B1.configure(command=Hello)
B2.configure(command=Hi)






GUI.mainloop()