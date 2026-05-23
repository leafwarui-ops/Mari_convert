
from PIL import Image  
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os

class file_convert:

    path = ""

    def ler_imagem (self):
        self.path = filedialog.askopenfilename(filetypes = [("",".webp")])

    def save_jpg(self):
        img = Image.open(self.path)
        img = img.convert("RGB")

        img_name = os.path.splitext(os.path.basename(self.path))[0]
        img_path = filedialog.askdirectory()
        end_path = os.path.join(img_path, img_name + ".jpg")

        img.save(end_path)
        messagebox.showinfo("arquivo salvo", "imagem salva com sucesso!")





