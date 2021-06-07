from tkinter import *
import calendar

def showCal2019() :
    calendarWindow = Tk()   
    calendarWindow.config(background = "#D9E1E1")
    calendarWindow.title(" CALENDER ")
    calendarWindow.geometry("550x600")
    getYear = 2019
    calendarContent = calendar.calendar(getYear)

    calendarYear = Label(calendarWindow, text = calendarContent, font = "Consolas 10 bold")
    calendarYear.grid(row = 5, column = 1, padx = 20)

    calendarWindow.mainloop()

def showCal2020() :
    calendarWindow = Tk()   
    calendarWindow.config(background = "#D9E1E1")
    calendarWindow.title(" CALENDER ")
    calendarWindow.geometry("550x600")
    getYear = 2020
    calendarContent = calendar.calendar(getYear)

    calendarYear = Label(calendarWindow, text = calendarContent, font = "Consolas 10 bold")
    calendarYear.grid(row = 5, column = 1, padx = 20)

    calendarWindow.mainloop()

def showCal2021() :
    calendarWindow = Tk()   
    calendarWindow.config(background = "#D9E1E1")
    calendarWindow.title(" CALENDER ")
    calendarWindow.geometry("550x600")
    getYear = 2021
    calendarContent = calendar.calendar(getYear)

    calendarYear = Label(calendarWindow, text = calendarContent, font = "Consolas 10 bold")
    calendarYear.grid(row = 5, column = 1, padx = 20)

    calendarWindow.mainloop()