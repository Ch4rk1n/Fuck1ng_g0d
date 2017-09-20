from tkinter import *

class janela():
    def __init__(self,tk):
        self.frame1 = Frame(tk)
        self.frame1.pack()
        self.frame2 = Frame(tk)
        self.frame2.pack()
        self.frame3 = Frame(tk)
        self.frame3.pack()

        self.textTela = label(self.frame1),text = 'Digite suas informações para cadastro')
        self.textTela.pack()
        self.textTela = label(self.frame2),text = 'Nome completo: ', font=('verdana'))
        self.campNome = Entry(self.frame2)
        self.campNome.pack(side=LEFT)

tk = Tk()
janela(tk)
tk.mainloop()