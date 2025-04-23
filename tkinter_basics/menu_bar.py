from tkinter import *
from tkinter.font import Font
from tkinter import messagebox

w=Tk()
w.title('Student App')
w.geometry("500x600")

#          STYLES
font_style1 = Font(family='times', size=30, weight='bold')
font_style2 = Font(family='times', size=18)
bg_color = 'lightpink'

#         STORAGE
student_details = {}
teacher_details = {}
login_details = {}


#       MAIN PAGE
welcome = Label(text='Welcome to our app', background=bg_color,
                font=font_style1)
welcome.pack(side='right', padx=80)

#    STUDENT LOGIN PAGE
def show_student_login_page():
    w1 = Toplevel()
    w1.geometry('400x400')
    w1.title('Student Login')

    stu = Label(w1,text='Login as student', font=font_style1)

    reg_no_l = Label(w1,text='Register no: ', font=font_style2, background=bg_color)
    password = Label(w1,text='Password: ', font=font_style2, background=bg_color)

    reg_no_e = Entry(w1, font=font_style2, width=8)
    pass_e = Entry(w1, font=font_style2, width=8)


    def save_student_details():
        print('Callign')
        import datetime as dt
        student_details[len(student_details)] = {
            'reg_no':reg_no_e.get(),
            'pass':pass_e.get(),
            'login_date_time': dt.datetime.now().strftime('%c') 
        }
        print(student_details)
        messagebox.showinfo('Login info', f'Reg no: {reg_no_e.get()} Login successfully..')

    submit = Button(w1, text='Submit', font=font_style2, fg=bg_color,
                    command=save_student_details,
                    activebackground='white'
                    )

    stu.place(x=50, y=70)
    reg_no_l.place(x=50, y=150)
    password.place(x=50, y=200)
    reg_no_e.place(x=200, y=150)
    pass_e.place(x=200, y=200)
    submit.place(x=180, y=300)


#   SHOW LOGIN DETAILS PAGE
def show_login_details():
    print(student_details)
    w2=Toplevel()
    w2.title('Login details')
    w2.geometry('600x600')
    heading = Label(text='Logged in details', font=font_style1)
    heading.pack(fill='both')
    for i in range(len(student_details)):
        result = f'''
        Reg no: {student_details[i]['reg_no']}
        Login Date and time: {student_details[i]['login_date_time']}
        '''
        rl = Label(w2, text=result, font=font_style2)
        rl.pack(fill='both')

        
menubar=Menu(w)

# LOGIN MENU
login_menu=Menu(menubar, tearoff=0)
login_menu.add_command(label='Login as student', command=show_student_login_page)
login_menu.add_command(label='Login as teacher')
menubar.add_cascade(label='Login', menu=login_menu)

# REGISTER MENU
register_menu=Menu(menubar, tearoff=0)
register_menu.add_command(label='Register as student')
register_menu.add_command(label='Register as teacher')
menubar.add_cascade(label='Register', menu=register_menu)

# SHOW MENU
show_menu=Menu(menubar, tearoff=0)
show_menu.add_command(label='Show login details', command=show_login_details)
show_menu.add_command(label='Show registered student')
show_menu.add_command(label='Show registered teacher')
menubar.add_cascade(label='Show', menu=show_menu)



w.config(background='lightpink', menu=menubar)
w.mainloop()
