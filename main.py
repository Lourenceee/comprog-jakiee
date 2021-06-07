from tkinter import *
from menus.menu import *
from menus.popupmenu import *
from functions.buttons import *
from functions.keybind import *
from widgets.canvas import *
from functions.mousebind import *

mainWindow = Tk()
mainWindow.geometry("400x500")
mainWindow.title("Jakiee")
icon = PhotoImage(file = 'images\logo.png')
openImg = PhotoImage(file = 'images\menu-img\openfile.png')
saveImg = PhotoImage(file = 'images\menu-img\savefile.png')
exitImg = PhotoImage(file = 'images\menu-img\exit.png')
mainWindow.iconphoto(True, icon)
mainWindow.config(background = "#080404")
header = PhotoImage(file = 'images\header.png')
mainWindow.bind("<Button-1>", mouseoneCor) #left mouse click
mainWindow.bind("<Button-2>", mousetwoCor) #scroll wheel
mainWindow.bind("<Button-3>", mousethreeCor) #right mouse click

menu = Menu(mainWindow)
mainWindow.config(menu = menu)

fileMenu = Menu(menu, tearoff = False, font = ('Racing Sans One', 10))
menu.add_cascade(label = 'File', menu = fileMenu, font = ('Racing Sans One', 10))
widgetsMenu = Menu(menu, tearoff = False, font = ('Racing Sans One', 10))
menu.add_cascade(label = 'Widgets', menu = widgetsMenu, font = ('Racing Sans One', 10))

fileMenu.add_cascade(label = 'Open Image', command = openFile, image = openImg, font = ('Racing Sans One', 10), compound = 'left')
fileMenu.add_separator()
fileMenu.add_cascade(label = 'Exit', command = exitFile, image = exitImg, font = ('Racing Sans One', 10), compound = 'left')

widgetsMenu.add_cascade(label = 'Canvas', command = showCanvas, image = exitImg, font = ('Racing Sans One', 10), compound = 'left')

headerlabel = Label(mainWindow, image = header).pack()


headerlabel = Label(mainWindow, text = 'left ctrl + j', font = ('Racing Sans One', 8,'italic'), background = '#FAE8E0').place(x=53, y=103)
mainWindow.bind('<Control_L><j>', ctrlj)

headerlabel = Label(mainWindow, text = 'left ctrl + h', font = ('Racing Sans One', 8,'italic'), background = '#FAE8E0').place(x=171, y=103)
mainWindow.bind('<Control_L><h>', ctrlh)

headerlabel = Label(mainWindow, text = 'left ctrl + k', font = ('Racing Sans One', 8,'italic'), background = '#FAE8E0').place(x=289, y=103)
mainWindow.bind('<Control_L><k>', ctrlk)

mainWindow.mainloop()