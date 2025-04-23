from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
from tkinter import ttk

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
    error = Label(text='You reached the year limit', fg='red', bg='black', font=inputfnt)
    
    if int(year_spinner.get()) >= int(year_spinner.cget('to')):
        error.place(x=600, y=150)
    else:
        print('else')
        error.destroy()

year_spinner = Spinbox(w,width=6,font=inputfnt, from_=2000, to=3000, command=year_func, state='readonly')
year_spinner.place(x=520, y=150)
#######################################################################################


e3 = Entry(w,font=inputfnt, background='white', fg='black',borderwidth=2)
e3.place(x=400, y=200)

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
    messagebox.showinfo('Information', concat_txt)

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

clear = Button(w,text='Clear', font=btnfont, bg='white', fg='black',
              command=clear_message,
               activebackground='black')
clear.place(x=550, y=550)

w.geometry("1000x700")
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