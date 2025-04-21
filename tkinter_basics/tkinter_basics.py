from tkinter import *
from tkinter.font import Font
from tkinter import messagebox

w = Tk()

w.title('Basics Application')

myfont=Font(family="times",size=20,weight="bold")
btnfont=Font(family="times",size=18, weight='bold')
inputfnt = Font(family="times",size=18)

l1 = Label(w,text='Name: ', font=myfont, fg='white', bg='black')
l1.place(x=100, y=100)

l2 = Label(w,text='Age: ', font=myfont, fg='white', bg='black')
l2.place(x=100, y=150)

l3 = Label(w,text='Salary: ', font=myfont, fg='white', bg='black')
l3.place(x=100, y=200)

l4 = Label(w,text='Department: ', font=myfont, fg='white', bg='black')
l4.place(x=100, y=250)

l5 = Label(w,text='Designation: ', font=myfont, fg='white', bg='black')
l5.place(x=100, y=300)

l6 = Label(w,text='Gender: ', font=myfont, fg='white', bg='black')
l6.place(x=100, y=350)

l7 = Label(w,text='Language knows: ', font=myfont, fg='white', bg='black')
l7.place(x=100, y=440)

e1 = Entry(w,font=inputfnt, background='white', fg='black')
e1.place(x=400, y=100)

e2 = Entry(w,font=inputfnt, background='white', fg='black')
e2.place(x=400, y=150)

e3 = Entry(w,font=inputfnt, background='white', fg='black')
e3.place(x=400, y=200)

e4 = Entry(w,font=inputfnt, background='white', fg='black')
e4.place(x=400, y=250)

e5 = Entry(w,font=inputfnt, background='white', fg='black')
e5.place(x=400, y=300)
def show_message():
    global r_result
    r_result = ''
    if r_var.get() == 1:
        r_result = male_r.cget('text')
    elif r_var.get() == 2:
        r_result = female_r.cget('text')
    elif r_var.get() == 3:
        r_result = others_r.cget('text')
    
    result = []
    if cbvar1.get() == 1:
        result.append(cb1.cget('text'))
        print(1)
    if cbvar2.get() == 1:
        result.append(cb2.cget('text'))
        print(2)
    if cbvar3.get() == 1:
        result.append(cb3.cget('text'))
        print(3)
    

    t1 = e1.get()
    t2 = e2.get()
    t3 = e3.get()
    t4 = e4.get()
    t5 = e5.get()
    concat_txt= f'''
    Name: {t1} 
    Age: {t2} 
    Salary: {t3} 
    Department: {t4} 
    Designation: {t5}
    Gender: {r_result}
    Language knows: {','.join(result)}
    '''
    messagebox.showinfo('Information', concat_txt)

def clear_message():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)

    cb3.deselect()
    cb1.deselect()
    cb2.deselect()

    r_var.set(None)
r_var = IntVar()

male_r = Radiobutton(w, text='Male', value=1, variable=r_var)
male_r.place(x=400, y=350)

female_r = Radiobutton(w, text='Female', value=2, variable=r_var)
female_r.place(x=400, y=380)

others_r = Radiobutton(w, text='Others', value=3, variable=r_var)
others_r.place(x=400, y=410)

cbvar1 = IntVar()
cb1 = Checkbutton(w, text='Tamil',
                  variable=cbvar1,
                  onvalue=1,
                  offvalue=0)

cb1.place(x=400, y=450)
cbvar2 = IntVar()
cb2 = Checkbutton(w, text='English',
                  variable=cbvar2,
                  onvalue=1,
                  offvalue=0)
cb2.place(x=400, y=480)

cbvar3 = IntVar()
cb3 = Checkbutton(w, text='Hindi',
                   variable=cbvar3,
                  onvalue=1,
                  offvalue=0)
cb3.place(x=400, y=510)

show = Button(w,text='Submit', font=btnfont, bg='white', fg='black',
              command=show_message)
show.place(x=400, y=550)

clear = Button(w,text='Clear', font=btnfont, bg='white', fg='black',
              command=clear_message)
clear.place(x=550, y=550)

w.geometry("1000x700")
w.config(bg='black')
w.mainloop()

