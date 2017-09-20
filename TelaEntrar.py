from tkinter import *

janela=Tk()

lb=Label (janela, text="Usuário",background = "Yellow")
lb.place(x=460, y=100)
lb['font'] = 'Helvetica 30 bold'

ed=Entry(janela)
ed.place(x=460, y=150)
ed['font'] = 'Helvetica 20 bold'

lb=Label (janela, text="Senha",background = "Yellow")
lb.place(x=460, y=200)
lb['font'] = 'Helvetica 30 bold'

ed2=Entry(janela)
ed2.place(x=460, y=250)
ed2['font'] = 'Helvetica 20 bold'

janela.mainloop()

