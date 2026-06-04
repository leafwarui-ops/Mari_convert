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
        root.frame_top = Frame(root)
        root.frame_bottom = Frame(root)
        root.frame_top.pack(side = "top")
        root.frame_bottom.pack(side = "bottom")
        root.lbl_title = Label(root.frame_top, text = "Mari Converter", font = ("Nunito", 20))
        root.lbl_title.pack(anchor = "center")
    
    #função que exibe a janela
    def iniciar(root):
        root.mainloop()
    
    #função que cria botões automaticamente ao receber um array
    def buttons(root, dados):
        for dado in dados:
            btn = Button(root.frame_bottom, text = dado["titulo"], command = dado["function"])
            btn.pack(side= "left", padx = 5, pady = 100)
    
    #cria o popup que permite o usuario decidir qual o formato que ele deseja converter o arquivo
    def janela(root, files, formato):
        janela = Toplevel()
        janela.title("Formato")
        janela.geometry('300x300')
        frame_top = Frame(janela)
        frame_bottom = Frame(janela)
        frame_top.pack(side = "top")
        frame_bottom.pack(side = "bottom")
        
        lbl_title = Label(frame_top, text ="Mari Converter", font = ("Nunito", 20))
        lbl_title.pack(anchor = "center")

        #match que define quais botões de formato de conversão devem aparecer 
        match formato:
            case ".webp":
                dados = [
                {"titulo":"jpg","function": lambda: files.save_jpg(janela)},
                {"titulo":"png","function": lambda: files.save_png(janela)},
                {"titulo":"bmp","function": lambda: files.save_bmp(janela)}
                ]
            case ".jpg":
                dados = [
                {"titulo":"webp","function": lambda: files.save_webp(janela)},
                {"titulo":"png","function": lambda: files.save_png(janela)},
                {"titulo":"bmp","function": lambda: files.save_bmp(janela)}
                ]
            case ".png":
                dados = [
                {"titulo":"jpg","function": lambda: files.save_jpg(janela)},
                {"titulo":"webp","function": lambda: files.save_webp(janela)},
                {"titulo":"bmp","function": lambda: files.save_bmp(janela)}
                ]
            case ".bmp":
                dados = [
                {"titulo":"jpg","function": lambda: files.save_jpg(janela)},
                {"titulo":"webp","function": lambda: files.save_webp(janela)},
                {"titulo":"png","function": lambda: files.save_png(janela)}
                ]
        #cria os botões necessarios na tela
        for dado in dados:
            btn = Button(frame_bottom, text = dado["titulo"], command = dado["function"])
            btn.pack(side = "left", padx = 5, pady = 100)

        





#classe de conversão

class file_convert:

    #abre os arquivos para que o usuario escolha o arquivo do formato desejado
    def ler_imagem(self,formato):
        self.path = filedialog.askopenfilename(filetypes = [("",formato)])
        App.janela(App, self, formato)

    #salva arquivos para jpg
    def save_jpg(self, janela):
        img = Image.open(self.path)
        img = img.convert("RGB")

        img_name = os.path.splitext(os.path.basename(self.path))[0]
        img_path = filedialog.askdirectory()
        end_path = os.path.join(img_path, img_name + ".jpg")

        img.save(end_path)
        messagebox.showinfo("arquivo salvo", "imagem salva com sucesso!")
        janela.destroy()

    #salva arquivos para wepb
    def save_webp(self, janela):
        img = Image.open(self.path)
        
        img_name = os.path.splitext(os.path.basename(self.path))[0]
        img_path = filedialog.askdirectory()
        end_path = os.path.join(img_path, img_name + ".webp")

        img.save(end_path)
        messagebox.showinfo("arquivo salvo", "imagem salva com sucesso!")
        janela.destroy()

    #salva arquivos para png
    def save_png(self, janela):
        img = Image.open(self.path)
        img = img.convert("RGBA")
        
        img_name = os.path.splitext(os.path.basename(self.path))[0]
        img_path = filedialog.askdirectory()
        end_path = os.path.join(img_path, img_name + ".png")

        img.save(end_path)
        messagebox.showinfo("arquivo salvo", "imagem salva com sucesso!")
        janela.destroy()

    def save_bmp(self, janela):
        img = Image.open(self.path)

        img_name = os.path.splitext(os.path.basename(self.path))[0]
        img_path = filedialog.askdirectory()
        end_path = os.path.join(img_path, img_name + ".bmp")

        img.save(end_path)
        messagebox.showinfo("arquivo salvo", "imagem salva com sucesso!")
        janela.destroy()




