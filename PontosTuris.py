from tkinter import *

janela=Tk()

lb=Label (janela, text="Pontos Turisticos",background = "Yellow")
lb.place(x=450, y=10)
lb['font'] = 'Helvetica 30 bold'

b1 = Button(janela, width=20, text="Arena do Grêmio", background="green")
b1.place(x=490, y=70)
b1['font'] = 'Helvetica 15 bold'

b2 = Button(janela, width=20, text="Beira Rio", background="green")
b2.place(x=490, y=120)
b2['font'] = 'Helvetica 15 bold'

b3 = Button(janela, width=20, text="Casa de cultura", background="green")
b3.place(x=490, y=170)
b3['font'] = 'Helvetica 15 bold'

b4 = Button(janela, width=20, text="Cidade Baixa", background="green")
b4.place(x=490, y=220)
b4['font'] = 'Helvetica 15 bold'

b5 = Button(janela, width=20, text="Gasômetro", background="green")
b5.place(x=490, y=270)
b5['font'] = 'Helvetica 15 bold'

b6 = Button(janela, width=20, text="Laçador", background="green")
b6.place(x=490, y=320)
b6['font'] = 'Helvetica 15 bold'

b6 = Button(janela, width=20, text="Mercado Público", background="green")
b6.place(x=490, y=370)
b6['font'] = 'Helvetica 15 bold'

b6 = Button(janela, width=20, text="Guaíba", background="green")
b6.place(x=490, y=420)
b6['font'] = 'Helvetica 15 bold'

b6 = Button(janela, width=20, text="Praça da Matriz", background="green")
b6.place(x=490, y=470)
b6['font'] = 'Helvetica 15 bold'






janela.mainloop()