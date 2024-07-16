from tkinter import * 
import tkinter as tk
from PIL import ImageTk,Image
import cv2


root = Tk()
root.title("Docker on Steroids")

root.geometry('1200x800')
root.configure(background="#FFA500")
text_label = Label(root,text="Docker on Steroids",fg='black',bg='#FFA500')
text_label.pack(pady=(10,10))
text_label.config(font=("Vandana",25))
root.mainloop()

