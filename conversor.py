from tkinter import *
from PIL import Image
from tkinter import filedialog
from tkinter import messagebox
import os

class App(Tk):

    

    #função que define os parametros da janela
    def __init__(root,nome):
        super().__init__()
        root.title(nome)
        root.geometry("300x300")
        root.frame = Frame(root)
        root.frame.pack()
    
    #função que exibe a janela
    def iniciar(root):
        root.mainloop()
    
    #função que cria botões automaticamente ao receber um array
    def buttons(root, dados):
        for dado in dados:
            btn = Button(root, text = dado["titulo"], command = dado["function"])
            btn.pack()
    
    #cria o popup que permite o usuario decidir qual o formato que ele deseja converter o arquivo
    def janela(root, files, formato):
        janela = Toplevel()
        janela.title("Formato")
        janela.geometry('300x300')
        frame1 = Frame(janela)
        frame1.pack()
        
        #match que define quais botões de formato de conversão devem aparecer 
        match formato:
            case ".webp":
                dados = [
                {"titulo":"jpg","function": lambda: files.save_webp_jpg(janela)}
                ]
            case ".jpg":
                dados = [
                {"titulo":"webp","function": lambda: files.save_jpg_webp(janela)}
                ]
        #cria os botões necessarios na tela
        for dado in dados:
            btn = Button(janela, text = dado["titulo"], command = dado["function"])
            btn.pack()

        





#classe de conversão

class file_convert:

    #abre os arquivos para que o usuario escolha o arquivo do formato desejado
    def ler_imagem(self,formato):
        self.path = filedialog.askopenfilename(filetypes = [("",formato)])
        App.janela(App, self, formato)

    #salva arquivos webp para jpg
    def save_webp_jpg(self, janela):
        img = Image.open(self.path)
        img = img.convert("RGB")

        img_name = os.path.splitext(os.path.basename(self.path))[0]
        img_path = filedialog.askdirectory()
        end_path = os.path.join(img_path, img_name + ".jpg")

        img.save(end_path)
        messagebox.showinfo("arquivo salvo", "imagem salva com sucesso!")
        janela.destroy()

    #salva arquivos jpg para wepb
    def save_jpg_webp(self, janela):
        img = Image.open(self.path)
        
        img_name = os.path.splitext(os.path.basename(self.path))[0]
        img_path = filedialog.askdirectory()
        end_path = os.path.join(img_path, img_name + ".webp")

        img.save(end_path)
        messagebox.showinfo("arquivo salvo", "imagem salva com sucesso!")
        janela.destroy()





