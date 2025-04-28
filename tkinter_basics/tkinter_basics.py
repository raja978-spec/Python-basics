from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog

w = Tk()

w.title('Basics Application')

myfont=Font(family="times",size=20,weight="bold")
btnfont=Font(family="times",size=18, weight='bold')
inputfnt = Font(family="times",size=15, weight='bold')

l1 = Label(w,text='Name: ', font=myfont, fg='white', bg='black')
l1.place(x=100, y=100)

l2 = Label(w,text='Date of birth(D/M/Y):', font=myfont, fg='white', bg='black')
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

e1 = Entry(w,font=inputfnt, background='white', fg='black', borderwidth=2)
e1.place(x=400, y=100)

day_spinner = Spinbox(w,width=3,font=inputfnt, from_=1, to=31)
day_spinner.place(x=400, y=150)

month_spinner = Spinbox(w,width=3,font=inputfnt, from_=1, to=12)
month_spinner.place(x=460, y=150)


###################################PROBLEM PART#############################################
def year_func():
    error = Label(w,text='You reached the year limit', fg='red', bg='black', font=inputfnt)
    error.place(x=600, y=150)
    if int(year_spinner.get()) >= int(year_spinner.cget('to')):
        print('if')
    else:
        print('else')
        error.destroy()
year_spinner = Spinbox(w,width=6,font=inputfnt, from_=2000, to=3000, command=year_func)
year_spinner.place(x=520, y=150)
#######################################################################################


e3 = Entry(w,font=inputfnt, background='white', fg='black',borderwidth=2)
e3.place(x=400, y=200)
saved_info = ''
saved_info_date = ''

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
    if cbvar2.get() == 1:
        result.append(cb2.cget('text'))
    if cbvar3.get() == 1:
        result.append(cb3.cget('text'))
    
    age = f'{day_spinner.get()}/{month_spinner.get()}/{year_spinner.get()}'
    department = department_dropdown_box.get()
    
    t1 = e1.get()
    t3 = e3.get()
    t5 = e5.get()
    concat_txt= f'''
    Name: {t1} 
    DOB: {age} 
    Salary: {t3} 
    Department: {department} 
    Designation: {t5}
    Gender: {r_result}
    Language knows: {','.join(result)}
    '''
    saved_info += concat_txt
    import datetime as dt
    saved_info_date += f"{dt.datetime.now('%c')}"
    messagebox.showinfo('Information', concat_txt)

def show_edit_box():
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
    if cbvar2.get() == 1:
        result.append(cb2.cget('text'))
    if cbvar3.get() == 1:
        result.append(cb3.cget('text'))
    
    age = f'{day_spinner.get()}/{month_spinner.get()}/{year_spinner.get()}'
    department = department_dropdown_box.get()
    
    t1 = e1.get()
    t3 = e3.get()
    t5 = e5.get()
    concat_txt= f'''
    Name: {t1} 
    DOB: {age} 
    Salary: {t3} 
    Department: {department} 
    Designation: {t5}
    Gender: {r_result}
    Language knows: {','.join(result)}
    '''
    tp = Toplevel(w)
    result_l = Label(tp,text='Your entered details')
    result_l.pack()
    text = Text(tp)
    text.insert(END,concat_txt)
    text.pack()
    menu_bar = Menu(w)
    f_menu = Menu(menu_bar,tearoff=0)
    
    def save_content():
        file = filedialog.asksaveasfile(mode="w", defaultextension=".txt", filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
        if file:
            contents = text.get("1.0", "end")
            file.write(contents)
            file.close()

    def open_file_content():
        file = filedialog.askopenfile(mode="rb", title="Open a file")
        if file:
            contents = file.read()
            
            text.delete("1.0", "end")
            text.insert("1.0", contents)
            file.close()
                    
    f_menu.add_command(label='Open', command=open_file_content)
    f_menu.add_command(label='Save', command=save_content)
    menu_bar.add_cascade(label='File', menu=f_menu,
                     activebackground='black')
    
    
    tp.geometry('500x500')
    tp.title('Edit form')
    tp.config(background='black', menu=menu_bar)
    tp.mainloop()

department_dropdown_box = ttk.Combobox(w, width=18,font=inputfnt, state='readonly')
department_dropdown_box['values'] = ('HR','Finance','IT','Marketing','Sales','Operations')
department_dropdown_box.current(1)
department_dropdown_box.place(x=400, y=250)


e5 = Entry(w,font=inputfnt, background='white', fg='black',borderwidth=2)
e5.place(x=400, y=300)

def clear_message():
    e1.delete(0, END)
    e3.delete(0, END)
    e5.delete(0, END)

    cb3.deselect()
    cb1.deselect()
    cb2.deselect()

    r_var.set(None)
    department_dropdown_box.set(None)

# day. mont spin box
r_var = IntVar()
r_style = Font(family="times",size=10, weight='bold')
male_r = Radiobutton(w, text='Male', value=1, variable=r_var, font=r_style)
male_r.place(x=400, y=350)

female_r = Radiobutton(w, text='Female', value=2, variable=r_var, font=r_style)
female_r.place(x=400, y=380)

others_r = Radiobutton(w, text='Others', value=3, variable=r_var, font=r_style)
others_r.place(x=400, y=410)

cbvar1 = IntVar()
cb1 = Checkbutton(w, text='Tamil',
                  variable=cbvar1,
                  onvalue=1,
                  offvalue=0,
                  font=r_style
                  )

cb1.place(x=400, y=450)
cbvar2 = IntVar()
cb2 = Checkbutton(w, text='English',
                  variable=cbvar2,
                  onvalue=1,
                  offvalue=0,
                  font=r_style)
cb2.place(x=400, y=480)

cbvar3 = IntVar()
cb3 = Checkbutton(w, text='Hindi',
                   variable=cbvar3,
                  onvalue=1,
                  offvalue=0,
                  font=r_style)
cb3.place(x=400, y=510)

show = Button(w,text='Submit', font=btnfont, bg='white', fg='black',
              command=show_message,
              activebackground='black'
              )
show.place(x=400, y=550)

submit_and_edit = Button(w,text='Submit & Edit', font=btnfont, bg='white', fg='black',
              command=show_edit_box,
              activebackground='black'
              )
submit_and_edit.place(x=500, y=550)

clear = Button(w,text='Clear', font=btnfont, bg='white', fg='black',
              command=clear_message,
               activebackground='black')
clear.place(x=680, y=550)

import os
file_names = ''
for i in os.listdir(os.curdir):
    if i.endswith('.txt'):
        file_names = i + '\n'
nb = ttk.Notebook(w)
f1 = Frame(nb, highlightcolor='green', highlightbackground='green', highlightthickness=2)
f1.pack()
l1 = Label(f1,text='Current dir saved file count', background='black',fg='white')
l1.grid(columnspan=1)
l2 = Label(f1,text=len(os.listdir(os.curdir)), background='black',fg='white')
l2.grid(columnspan=2)
nb.add(f1, text='show saved info')

f2 = Frame(nb, highlightcolor='red', highlightbackground='red', highlightthickness=2)
f2.pack()
l3 = Label(f2,text='Current dir file names', background='black',fg='white')
l3.grid(columnspan=1)
l4 = Label(f2,text=file_names, background='black',fg='white')
l4.grid(columnspan=2)

nb.add(f1, text='show saved info')

nb.add(f2, text='show saved info details')
nb.place(x=700, y=400)

w.geometry("1000x650")
w.config(bg='black')
w.mainloop()

'''
1. Human Resources (HR)
HR Executive

HR Manager

Talent Acquisition Specialist

HR Business Partner

Learning & Development Manager

2. Finance
Accountant

Financial Analyst

Finance Manager

Payroll Specialist

Chief Financial Officer (CFO)

3. Information Technology (IT)
IT Support Specialist

Systems Administrator

Network Engineer

IT Manager

Chief Information Officer (CIO)

4. Marketing
Marketing Executive

Social Media Manager

Digital Marketing Analyst

Marketing Manager

Chief Marketing Officer (CMO)

5. Sales
Sales Executive

Business Development Associate

Regional Sales Manager

Key Account Manager

Head of Sales

6. Operations
Operations Executive

Supply Chain Analyst

Logistics Manager

Operations Manager

VP of Operations

7. Product Development
Product Analyst

Product Manager

UX/UI Designer

Technical Product Manager

Head of Product

8. Engineering / Software Development
Software Engineer

Frontend Developer

Backend Developer

DevOps Engineer

Chief Technology Officer (CTO)

9. Customer Support / Service
Customer Service Representative

Technical Support Engineer

Customer Success Manager

Support Team Lead

Customer Experience Head

10. Legal
Legal Advisor

Compliance Officer

Contract Specialist

Legal Manager

General Counsel
'''