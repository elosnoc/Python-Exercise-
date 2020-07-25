from tkinter import *
GUI = Tk()
GUI.geometry('500x300')

B1 = Button(GUI,text='Hello')
B1.pack()

from tkinter import ttk
B2 = ttk.Button(GUI,text="hi")
B2.pack()

def HelloWorld():
    print('HelloWorld')

B1.configure(command=HelloWorld)
#B1.place(x=200,y=100) #position Button name B1



GUI.mainloop()
