import kivy
kivy.require('1.7.0')
 
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.widget import Widget
 
class Image(Image):
    pass
 
class app(App):
    def build(self):
        return Image(source='bocha-jogo.jpg',pos=(0,0),size=(800,800))

b1 = Button(janela, width=20, text="+", command=soma_click)
b1.pos(180,60)

 
if __name__ == '__main__':
    app().run()
