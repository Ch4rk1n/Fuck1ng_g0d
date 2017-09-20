from tkinter import *

janela=Tk()


b1 = Button(janela, width=20, text="Entrar", background="green")
b1.place(x=400, y=100)
b1['font'] = 'Helvetica 30 bold'
b2 = Button(janela, width=20, text="Criar conta", background="green")
b2.place(x=400, y=200)
b2['font'] = 'Helvetica 30 bold'

lb=Label (janela, text="PoaCultural", background = "Yellow")
lb.place(x=530, y=300)
lb['font'] = 'Helvetica 30 bold'


janela.mainloop()
