import tkinter as tk
from tkinter import *

main_win = tk.Tk()
main_win.title("Home")
main_win.geometry("400x400")

username = tk.StringVar()
password = tk.StringVar()

def btn1_onclick():
    uname=txt1.get()
    passw=txt2.get()
    print(uname)
    print(passw)
    

txt1 = tk.Entry(main_win,textvariable=username)
txt2 = tk.Entry(main_win,textvariable=password)
btn1 = tk.Button(main_win,text="Click ME !",command=btn1_onclick)

txt1.pack()
txt2.pack()
btn1.pack()


main_win.mainloop()