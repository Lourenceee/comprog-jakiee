from tkinter import *

def showCanvas(): 
    canvaWindow = Tk()
    canvaWindow.title("Canva")
    canvaWindow.config(background = "#D9E1E1")
    canvaWindow = Canvas(canvaWindow,height=500,width=500)
    canvaWindow.create_line(0,0,700,500,fill="blue",width=5)
    canvaWindow.create_line(0,500,500,0,fill="pink",width=5)
    canvaWindow.create_rectangle(50,50,250,250,fill="purple")
    points = [250,0,900,500,0,500]
    canvaWindow.create_polygon(points,fill="green",outline="orange",width=5)
    canvaWindow.create_arc(0,0,100,500,style=PIESLICE,start=270,width=5)
    canvaWindow.pack()

    canvaWindow.mainloop()