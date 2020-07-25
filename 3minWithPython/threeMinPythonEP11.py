from tkinter import *
from tkinter import ttk
import random
GUI= Tk()
GUI.geometry('500x300')

v_eng = StringVar()
v_th = StringVar()

L1 = ttk.Label(GUI,textvariable=v_eng,font=('Angsana New',30))
L1.pack()

L2 = ttk.Label(GUI,textvariable = v_th,font=('Angsana New',30))
L2.pack()

vocab ={'cat':'แมว', 'Dog':'หมา'}
vocab_eng = list(vocab.keys()) #convert to list
def Eng():
    v_eng.set(random.choice(vocab_eng))
    v_th.set('')
def Th():
    v_th.set(vocab[v_eng.get()])

B1 = ttk.Button(GUI,text='ENG',command=Eng)
B1.pack()

B2 = ttk.Button(GUI,text='TH',command=Th)
B2.pack()






GUI.mainloop()
