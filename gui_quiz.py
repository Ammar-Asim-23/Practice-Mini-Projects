from cProfile import label
import tkinter as tk
from tkinter import *
from turtle import color
from click import command


root=tk.Tk()

root.title("QUIZGAME")
root.geometry("700x600")
root.config(background="#ffffff")

def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    lbl.config(text = "Provided Input: "+inp)
  
  
inputtxt.pack()
  
# Button Creation
printButton = tk.Button(root,
                        text = "Print", 
                        command = printInput)
printButton.pack()
  
# Label Creation
lbl = tk.Label(root, text = "")
lbl.pack()







root.mainloop()