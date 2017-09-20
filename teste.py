from tkinter import *
root=Tk()

class novo:

        def __init__(self, janela):

            ##defini a Janela como uma frame
            self.caixa=Frame(janela)
            self.caixa.grid()

            ##Criei dois labels de exemplo
            self.l1 = Label(janela, text='Usuário: ')
            self.l1.grid()
            self.l2 = Label(janela, text='Senha: ')
            self.l2.grid()
            ##Botão que vai dar o comando para chamar outra função, cadastro no caso
            self.b=Button(janela, text='Criar Conta', command=self.cadastro)
            self.b.grid()

        ##Segunda função que representaria a segunda tela
        def cadastro(janela):
            self.jan=Toplevel()
            self.l=Label(self.jan, text='Digite seus dados para cadastrar!')
            self.l.grid()
            ##Esse botão,serve para chamar a função que vai destruir a janela atual
            b=Button(self.jan, text='Voltar', command=self.fecha_jan)
            b.grid()

            self.jan.geometry('300x200')
            self.jan.transient(root)#
            self.jan.focus_force()#
            self.jan.grab_set()#

        ##Função que destroi a janela atual...
        def fecha_jan(self, janela):
            self.jan.destroy(self, janela)


novo(root)

root.geometry('300x200')

root.mainloop()