from tkinter import *
w = Tk()

frame1=Frame(w, height=100, width=200, background='skyblue')
frame1.grid(row=0, column=0)

frame2=Frame(w, height=100, width=200, background='green')
frame2.grid(row=1, column=0)
    
btn = Button(w, text='click', command=frame1.destroy)
btn.grid(columnspan=2)

w.geometry('500x500')
w.mainloop()