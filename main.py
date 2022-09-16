from tkinter import *
from tkinter import messagebox
import time
import random

msginfomessage = 'test'
msginfo = 'test'


def createwindow():
    root = Tk()
    root.geometry('750x550')
    root.resizable(width=False, height=False)
    root.title('MultiTool')
    Button(root, font="Roman 18 bold", width='15', text="resizable True", command=lambda: root.resizable(width=True, height=True)).pack()
    Button(root, font="Roman 18 bold", width='15', text="resizable False", command=lambda: root.resizable(width=False, height=False)).pack()
    Button(root, font="Roman 18 bold", width='10', text="exit", command=lambda: quit()).pack()
    def bgchange():
        if random.randint(1, 5) == 1:
            root.configure(bg="yellow")
        if random.randint(1, 5) == 2:
            root.configure(bg="blue")
        if random.randint(1, 5) == 3:
            root.configure(bg="red")
        if random.randint(1, 5) == 4:
            root.configure(bg="pink")
        if random.randint(1, 5) == 5:
            root.configure(bg="brown")
    def bgrainbow():
        number = 1
        if number == 1:
            root.configure(bg="yellow")
            number = number + 1
            time.sleep(0.5)
        if number == 2:
            root.configure(bg="blue")
            number = number + 1
            time.sleep(0.5)
        if number == 3:
            root.configure(bg="red")
            number = number + 1
            time.sleep(0.5)
        if number == 4:
            root.configure(bg="pink")
            number = number - 3
        else:
            messagebox.showerror('ERROR', 'error')

    Button(root, font="Roman 18 bold", width='10', text="change bg", command=lambda: bgchange()).pack()
    Button(root, font="Roman 18 bold", width='12', text="rainbow bg", command=lambda: bgrainbow())

    def start():
        mainwindow = Tk()
        mw = mainwindow
        mw.title('test')
        mw.geometry('750x550')
        mw.resizable(width=True, height=False)
        def readfiles():
            Label(mainwindow, text="Имя файла (без формата)", font="Roman 12 bold").pack()
            filename = StringVar()
            Entry(mainwindow, textvariable=filename).pack()
            Label(mainwindow, text="Формат файла (без имени)", font="Roman 12 bold").pack()
            fileformat = StringVar()
            Entry(mainwindow, textvariable=fileformat).pack()
            def completefr():
                if fileformat.get() != '.kittm':
                    msginfomessage = 'ERROR'
                    msginfo = 'unkown file format'
                    messagebox.showerror('ERROR', message='unkown format')
                    time.sleep(2)
                    quit()
                if fileformat.get() == '.kittm':
                    fileopen = open(filename + fileformat , 'r')

            Button(mainwindow, font="Roman 18 bold", text="complete!", command=completefr).pack()
        Button(mainwindow, font="Roman 18 bold", width='10', text="file reader", command=readfiles).pack()


        mw.mainloop()

    root.mainloop()

createwindow()
