import tkinter as tk
from tkinter import *
from tkinter import messagebox

#setup basic
home = tk.Tk()
home.title("Calcultor")
home.geometry("500x400")
home.minsize(500,400)
home.maxsize(500,400)

#intializing variables for text retrival
number1 = tk.StringVar()
number2 = tk.StringVar()


# methods of calculator
def plusbtn_click():
   t1 = number1.get()
   t2 = number2.get()
   ans= int(t1)+int(t2)
   messagebox.showinfo("Addition",ans)
   print(ans)
    
def minusbtn_click():
   t1 = number1.get()
   t2 = number2.get()
   ans= int(t1)-int(t2)
   messagebox.showinfo("Substraction",ans)
   print(ans)

def multibtn_click():
   t1 = number1.get()
   t2 = number2.get()
   ans= int(t1)*int(t2)
   messagebox.showinfo("Multiplication",ans)
   print(ans)

def dividebtn_click():
   t1 = number1.get()
   t2 = number2.get()
   ans= int(t1)/int(t2)
   messagebox.showinfo("Divide",ans)
   print(ans)

#intializing componants
Title = tk.Label(text="Enter numbers")
num1 = tk.Entry(home,textvariable=number1)
num2 = tk.Entry(home,textvariable=number2)
plusbtn = tk.Button(home,text="  +  ",command=plusbtn_click)
minusbtn = tk.Button(home,text="  -  ",command=minusbtn_click)
multibtn = tk.Button(home,text="  *  ",command=multibtn_click)
dividebtn = tk.Button(home,text="  /  ",command=dividebtn_click)


#adding commonents to our frame
Title.pack()
num1.pack()
num2.pack()
plusbtn.pack()
minusbtn.pack()
multibtn.pack()
dividebtn.pack()



home.mainloop()