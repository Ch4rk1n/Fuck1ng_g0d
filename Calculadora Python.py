from tkinter import *
janela = Tk()
def soma_click():
    num1=float(ed.get())
    num2=float(ed2.get())
    lb["text"] = num1+num2

def sub_click():
    num1=float(ed.get())
    num2=float(ed2.get())
    lb["text"] = num1-num2

def div_click():
    num1=float(ed.get())
    num2=float(ed2.get())
    lb["text"] = num1/num2

def multi_click():
    num1=float(ed.get())
    num2=float(ed2.get())
    lb["text"] = num1*num2

ed=Entry(janela)
ed.place(x=50, y=60)

ed2=Entry(janela)
ed2.place(x=50, y=100)

b1 = Button(janela, width=20, text="+", command=soma_click)
b1.place(x=180, y=60)

b2 = Button(janela, width=20, text="-", command=sub_click)
b2.place(x=180, y=100)

b3 = Button(janela, width=20, text="/", command=div_click)
b3.place(x=180, y=140)

b4 = Button(janela, width=20, text="*", command=multi_click)
b4.place(x=180, y=180)

lb=Label (janela, text="")
lb.place(x=50, y=180)

janela.title("Calculadora")
janela.geometry("800x800")
janela.mainloop()
