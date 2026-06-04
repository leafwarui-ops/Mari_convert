from tkinter import *
from conversor import *

#chamando a classe app dando o nome da janela
main = App("Mari converter")
#chamando a classe file_convert e instanciando-a
files = file_convert()

#array que define os botões de conversão
dados_ler = [
    {"titulo":"webp","function": lambda: files.ler_imagem(".webp")}, #botão webp
    {"titulo":"jpg","function": lambda: files.ler_imagem(".jpg")}, #botão jpg
    {"titulo":"png","function": lambda: files.ler_imagem(".png")}, #botão png
    {"titulo":"bmp","function": lambda: files.ler_imagem(".bmp")}, #botão btm
    ]


#cria os botões na tela
App.buttons(main, dados_ler)

#iniciando o programa
main.iniciar()