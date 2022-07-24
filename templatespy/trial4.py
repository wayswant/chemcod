import tkinter
from tkinter import *

window = Tk()
window.geometry("420x420")
window.title("GUI program")

# icon = PhotoImage(file='purple.png')
# window.iconphoto(True, icon)

photo = PhotoImage(file='purple.png')

window.configure(background="white")

label = Label(window, text="Hello World",
              # image=photo
              )
label.pack()

window.mainloop()

