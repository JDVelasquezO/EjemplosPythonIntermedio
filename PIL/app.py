from tkinter import *
from PIL import Image, ImageTk, ImageOps, ImageFilter

root = Tk()
root.title("Imagen en Tikinter con PIL")
root.geometry("500x500")

# 1. Abre la imagen y la sube a python
img = Image.open('Harpsichord.png')

# 2. Modifica la imagen original
img = img.resize((400, 400), Image.Resampling.LANCZOS)
# img = img.rotate(60)
# img = img.convert("L")
# img = ImageOps.invert(img.convert("RGB"))
# img = img.filter(ImageFilter.BLUR)
# img = img.filter(ImageFilter.FIND_EDGES)
# img = img.filter(ImageFilter.SMOOTH)
# img = img.filter(ImageFilter.EDGE_ENHANCE)
# img = img.filter(ImageFilter.SHARPEN)
# img = img.convert("1")
# img = ImageOps.posterize(img, bits=5)
# img = ImageOps.solarize(img, threshold=256)

# 3. Mete la imagen en tkinter
img = ImageTk.PhotoImage(img)

lblImg = Label(root, image=img)
lblImg.pack()

def cambiarBlancoNegro():
    global img
    global lblImg
    img = img.convert("1")
    img = ImageTk.PhotoImage(img)
    lblImg = Label(root, image=img)
    lblImg.pack()

b1 = Button(root, text="Cambiar imagen", command=cambiarBlancoNegro)
b1.pack()

root.mainloop()
