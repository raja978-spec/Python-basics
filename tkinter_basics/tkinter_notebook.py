# from tkinter import *
# from tkinter import ttk

# w = Tk()
# '''
# It allows to hold more than one page in 
# single screen

# columnspan is combination of row and columns
# '''

# nb = ttk.Notebook(w)
# nb.pack()

# frame1= Frame(nb,width=200, height=100, highlightbackground='blue', 
#               highlightthickness=1)

# nb.add(frame1, text='Nav 1')

# frame2= Frame(nb,width=200, height=100, highlightbackground='red', 
#               highlightthickness=1)
# frame2.grid(columnspan=2)
# nb.add(frame2,text='Nav 2')

# w.title('Basic of notebook')
# w.geometry('500x500')
# w.mainloop()

import tkinter
from tkinter import Label, Entry, Button, IntVar, Checkbutton
from tkinter.font import Font
from tkinter import messagebox
from tkinter.ttk import Radiobutton

form = tkinter.Tk()
form.geometry("600x500")
form.title("Form")
form.config(bg="gray")
font_1 = Font(family="times",size=14,weight="bold")
font_2 = Font(family="times",size=25,weight="bold")

def clear():
    entry1.delete(0,tkinter.END)
    entry2.delete(0,tkinter.END)
    entry4.delete(0,tkinter.END)
    entry6.delete(0,tkinter.END)
    s_1.deselect()
    s_2.deselect()
    s_3.deselect()
    g_f.set(None)


def submit():
    com_sub = []
    if sub1.get() == 1:
        get1 = s_1.cget("text")
        com_sub.append(get1)
    if sub2.get() == 1:
        get2 = s_2.cget("text")
        com_sub.append(get2)
    if sub3.get() == 1:
        get3 = s_3.cget("text")
        com_sub.append(get3)
    if sub1.get() == 0 and sub2.get() == 0 and sub3.get() == 0:
        com_sub = "None"


    print(com_sub)

    s_gender = g_f.get()
    name = entry1.get()
    age = entry2.get()
    phone = entry4.get()
    address = entry6.get()
    all_entry = f"Name:{name}\nAge:{age}\nGender:{s_gender}\nPhone:{phone}\nSubject:{com_sub}\nAddress:{address}"
    messagebox.showinfo("Information",all_entry)

title_l = Label(form,text="Form",font=font_2,bg="black",fg="white",padx=10,pady=5,relief="raised")
title_l.pack()

g_f = tkinter.StringVar()
sub1 = IntVar()
sub2 = IntVar()
sub3 = IntVar()

name_l = Label(form,text="Name:",font=font_1,bg="gray")
name_l.place(x=100,y=120)
age_l = Label(form,text="Age:",font=font_1,bg="gray")
age_l.place(x=100,y=160)
gender_l = Label(form,text="Gender:",font=font_1,bg="gray")
gender_l.place(x=100,y=200)
phone_l = Label(form,text="Phone:",font=font_1,bg="gray")
phone_l.place(x=100,y=240)
subject_l = Label(form,text="Subject:",font=font_1,bg="gray")
subject_l.place(x=100,y=280)
address_l = Label(form,text="Address:",font=font_1,bg="gray")
address_l.place(x=100,y=320)

entry1 = Entry(form,width=20,font=font_1,bg="white",fg="black",relief="ridge")
entry1.place(x=200,y=120)
entry2 = Entry(form,width=20,font=font_1,bg="white",fg="black",relief="ridge")
entry2.place(x=200,y=160)
entry4 = Entry(form,width=20,font=font_1,bg="white",fg="black",relief="ridge")
entry4.place(x=200,y=240)
entry6 = Entry(form,width=20,font=font_1,bg="white",fg="black",relief="ridge")
entry6.place(x=200,y=320)

s_1 = Checkbutton(form,text="Tamil",variable=sub1,bg="gray",fg="black",font=font_1,onvalue=1,offvalue=0)
s_1.place(x=200,y=280)
s_2 = Checkbutton(form,text="English",variable=sub2,bg="gray",fg="black",font=font_1,onvalue=1,offvalue=0)
s_2.place(x=300,y=280)
s_3 = Checkbutton(form,text="Maths",variable=sub3,bg="gray",fg="black",font=font_1,onvalue=1,offvalue=0)
s_3.place(x=400,y=280)

gender_m = Radiobutton(form,text="Male",variable=g_f,value="Male")
gender_m.place(x=200,y=200)
gender_f = Radiobutton(form,text="female",variable=g_f,value="Female")
gender_f.place(x=280,y=200)

s_button = Button(form,text="Submit",font=font_1,bg="white",fg="black",activebackground="black",activeforeground="white",relief="raised",command=submit)
s_button.place(x=200,y=380)
c_button = Button(form,text="Cancel",font=font_1,bg="white",fg="black",activebackground="black",activeforeground="white",relief="raised",command=clear)
c_button.place(x=200,y=440)
form.mainloop()


import tkinter
from tkinter import *
from tkinter import Label, Entry, Button, IntVar, Checkbutton, Spinbox
from tkinter.font import Font
from tkinter import messagebox, Menu, Toplevel, Text, filedialog
from tkinter.ttk import Radiobutton
from tkinter import ttk

form = tkinter.Tk()
form.geometry("700x600")
form.title("Form")
form.config(bg="#106EBE")
font_1 = Font(family="times",size=14,weight="bold")
font_2 = Font(family="times",size=25,weight="bold")
font_3 = Font(family="times",size=14)

all_entry =""


def clear():
    entry1.delete(0,tkinter.END)
    entry2.delete(0,tkinter.END)
    entry4.delete(0,tkinter.END)
    entry6.delete(0,tkinter.END)
    s_1.deselect()
    s_2.deselect()
    s_3.deselect()
    g_f.set(None)
    DOB_d.delete(0,tkinter.END)
    DOB_m.delete(0, tkinter.END)
    DOB_y.delete(0, tkinter.END)
    pro_l.current(0)


def submit():
    global all_entry
    com_sub = []
    if sub1.get() == 1:
        get1 = s_1.cget("text")
        com_sub.append(get1)
    if sub2.get() == 1:
        get2 = s_2.cget("text")
        com_sub.append(get2)
    if sub3.get() == 1:
        get3 = s_3.cget("text")
        com_sub.append(get3)
    if sub1.get() == 0 and sub2.get() == 0 and sub3.get() == 0:
        com_sub = "None"

    s_gender = g_f.get()
    name = entry1.get()
    age = entry2.get()
    phone = entry4.get()
    address = entry6.get()
    lang = pro_l.get()
    DOB_s = f"{DOB_d.get()}/{DOB_m.get()}/{DOB_y.get()}"
    all_entry = f"Name:{name}\nAge:{age}\nGender:{s_gender}\nDOB:{DOB_s}\nPhone:{phone}\nSubject:{com_sub}\nLanguage:{lang}\nAddress:{address}"
    messagebox.showinfo("Information",all_entry)


def submit_edit():
    submit()
    global all_entry
    form1 = tkinter.Tk()
    form1.geometry("700x600")
    form1.title("Note")
    form1.config(bg="#E7473C")


    def new():
        text_a.delete(0, tkinter.END)

    def open_file():
        file_path = filedialog.askopenfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, 'r') as file:
                text_a.delete(1.0, tkinter.END)
                text_a.insert(tkinter.END, file.read())

    def save_file():
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, 'w') as file:
                file.write(text_a.get(1.0, tkinter.END))

    def msg():
        global all_entry
        msg = Toplevel(form1)
        msg.geometry("400x400")
        msg.config(bg="#000000")
        msg.title("Show")
        lab_m = Label(msg, text="Nothing", font=("times",30,"bold"), fg="white", bg="#000000")
        lab_m.place(x=130,y=150)
        btn_m = Button(msg, text="Exit", font=font_1, width=10,bg="white", fg="black",relief="groove",command=msg.destroy)
        btn_m.pack(padx=10, pady=10)

    text_a = Text(form1)
    text_a.pack(expand=True)
    text_a.insert(tkinter.END,all_entry)

    menubar = Menu(form1)
    form1.config(menu=menubar)

    file_m = Menu(menubar, tearoff=0)
    file_m.add_command(label="New", command=new)
    file_m.add_command(label="Open", command=open_file)
    file_m.add_command(label="Save", command=save_file)
    file_m.add_command(label="Close", command=form1.quit)
    file_m.add_separator()
    file_m.add_command(label="Show",command=msg)
    menubar.add_cascade(label="File", menu=file_m)

    file_m1 = Menu(menubar, tearoff=0)
    file_m1.add_command(label="Clear",command=new)
    file_m1.add_command(label="Cut")
    file_m1.add_command(label="Paste")
    menubar.add_cascade(label="Edit", menu=file_m1)


title_l = Label(form,text="Form",font=font_2,bg="black",fg="white",padx=10,pady=5,relief="raised")
title_l.pack()

g_f = tkinter.StringVar()
sub1 = IntVar()
sub2 = IntVar()
sub3 = IntVar()

#lables
name_l = Label(form,text="Name:",font=font_1,bg="#106EBE")
name_l.place(x=100,y=120)
age_l = Label(form,text="Age:",font=font_1,bg="#106EBE")
age_l.place(x=100,y=160)
gender_l = Label(form,text="Gender:",font=font_1,bg="#106EBE")
gender_l.place(x=100,y=200)
DOB_l = Label(form,text="DOB:",font=font_1,bg="#106EBE")
DOB_l.place(x=100,y=240)
phone_l = Label(form,text="Phone:",font=font_1,bg="#106EBE")
phone_l.place(x=100,y=280)
subject_l = Label(form,text="Subject:",font=font_1,bg="#106EBE")
subject_l.place(x=100,y=320)
program_l = Label(form,text="Language:",font=font_1,bg="#106EBE")
program_l.place(x=100,y=360)
address_l = Label(form,text="Address:",font=font_1,bg="#106EBE")
address_l.place(x=100,y=400)

#entry
entry1 = Entry(form,width=20,font=font_1,bg="white",fg="black",relief="raised")
entry1.place(x=200,y=120)
entry2 = Entry(form,width=20,font=font_1,bg="white",fg="black",relief="raised")
entry2.place(x=200,y=160)
entry4 = Entry(form,width=20,font=font_1,bg="white",fg="black",relief="raised")
entry4.place(x=200,y=280)
entry6 = Entry(form,width=20,font=font_1,bg="white",fg="black",relief="raised")
entry6.place(x=200,y=400)

#checkbox-subject
s_1 = Checkbutton(form,text="Tamil",variable=sub1,bg="#106EBE",fg="black",font=font_1,onvalue=1,offvalue=0)
s_1.place(x=200,y=320)
s_2 = Checkbutton(form,text="English",variable=sub2,bg="#106EBE",fg="black",font=font_1,onvalue=1,offvalue=0)
s_2.place(x=300,y=320)
s_3 = Checkbutton(form,text="Maths",variable=sub3,bg="#106EBE",fg="black",font=font_1,onvalue=1,offvalue=0)
s_3.place(x=400,y=320)

#gender
gender_m = Radiobutton(form,text="Male",variable=g_f,value="Male")
gender_m.place(x=200,y=200)
gender_f = Radiobutton(form,text="female",variable=g_f,value="Female")
gender_f.place(x=280,y=200)

#spinbox
DOB_d = Spinbox(form,from_=1,to=31,width=2,font=font_3)
DOB_d.place(x=200,y=240)
DOB_m = Spinbox(form,from_=1,to=12,width=2,font=font_3)
DOB_m.place(x=240,y=240)
DOB_y = Spinbox(form,from_=1980,to=2020,width=5,font=font_3)
DOB_y.place(x=280,y=240)

#combobox
pro_l = ttk.Combobox(form,width=20,state="readonly")
pro_l["values"]=("C","C++","java","python")
pro_l.current(0)
pro_l.place(x=200,y=360)



s_button = Button(form,text="Submit",font=font_1,bg="white",fg="black",activebackground="black",activeforeground="white",relief="raised",command=submit)
s_button.place(x=200,y=440)
c_button = Button(form,text="Cancel",font=font_1,bg="white",fg="black",activebackground="black",activeforeground="white",relief="raised",command=clear)
c_button.place(x=300,y=440)
s_button1 = Button(form,text="Submit and Edit",font=font_1,bg="white",fg="black",activebackground="black",activeforeground="white",relief="raised",command=submit_edit)
s_button1.place(x=200,y=500)

form.mainloop()

# from tkinter import messagebox
# a=dog1.jpg
# def show_info():
#     # Display the message box with title and message
#     messagebox.showinfo(
#         title="Information",
#         message="This is an information message.",
#         icon=a  # This is just an example; 'icon' is typically not supported by showinfo
#     )
#
# root = Tk()
# root.geometry("300x200")
# root.title("Info Message Example")
#
# info_button = Button(root, text="Show Info", command=show_info, bg="blue", fg="white")
# info_button.pack(pady=20)
#
# root.mainloop()


from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk  # Pillow for image handling

def show_custom_info():
    # Create a new Toplevel window for the custom message box
    custom_box = Toplevel(root)
    custom_box.title("Information")
    custom_box.geometry("300x200")

    # Load the image
    img = Image.open("dog1.jpg")  # Ensure the image path is correct
    img = img.resize((100, 100), Image.ANTIALIAS)  # Resize the image if needed
    photo = ImageTk.PhotoImage(img)

    # Create a label for the image
    img_label = Label(custom_box, image=photo)
    img_label.image = photo  # Keep a reference to avoid garbage collection
    img_label.pack(pady=10)

    # Create a label for the message
    msg_label = Label(custom_box, text="This is an information message.")
    msg_label.pack(pady=10)

    # Create an OK button to close the custom message box
    ok_button = Button(custom_box, text="OK", command=custom_box.destroy)
    ok_button.pack(pady=10)

root = Tk()
root.geometry("300x200")
root.title("Custom Info Message Example")

info_button = Button(root, text="Show Info", command=show_custom_info, bg="blue", fg="white")
info_button.pack(pady=20)

root.mainloop()

pack(ipady=value)

import tkinter
from tkinter import *
from tkinter import Label, Entry, Button, IntVar, Checkbutton, Spinbox
from tkinter.font import Font
from tkinter import messagebox, Menu, Toplevel, Text, filedialog
from tkinter.ttk import Radiobutton
from tkinter import ttk

form = tkinter.Tk()
form.geometry("700x600")
form.title("form")
form.config(bg="#106EBE")
font_1 = Font(family="times", size=14, weight="bold")
font_2 = Font(family="times", size=25, weight="bold")
font_3 = Font(family="times", size=14)

all_entry = ""


def main():
    def submit_edit():


        submit()

        global all_entry

        notebook = ttk.Notebook(form)
        notebook.pack()

        frame1 = Frame(notebook, height=500, width=500)
        frame1.pack()
        frame2 = Frame(notebook, height=500, width=500, bg="#000000")
        frame2.pack()

        def new():
            text_a.delete(0, tkinter.END)

        def open_file():
            file_path = filedialog.askopenfilename(defaultextension=".txt")
            if file_path:
                with open(file_path, 'r') as file:
                    text_a.delete(1.0, tkinter.END)
                    text_a.insert(tkinter.END, file.read())

        def save_file():
            file_path = filedialog.asksaveasfilename(defaultextension=".txt")
            if file_path:
                with open(file_path, 'w') as file:
                    file.write(text_a.get(1.0, tkinter.END))

        	
        text_a.pack(expand=True)
        text_a.insert(tkinter.END, all_entry)

        lab_m = Label(frame2, text="Nothing", font=("times", 30, "bold"), fg="white", bg="#000000")
        lab_m.place(x=130, y=150)
        btn_m = Button(frame2, text="Exit", font=font_1, width=10, bg="white", fg="black", relief="groove",
                       command=frame2.destroy)
        btn_m.pack(padx=10, pady=10)

        notebook.add(frame1, text="Note")
        notebook.add(frame2, text="Show")

        menubar = Menu(form)
        form.config(menu=menubar)

        file_m = Menu(menubar, tearoff=0)
        file_m.add_command(label="New", command=new)
        file_m.add_command(label="Open", command=open_file)
        file_m.add_command(label="Save", command=save_file)
        file_m.add_command(label="Close", command=form.quit)
        file_m.add_separator()
        file_m.add_command(label="Show", command="")
        menubar.add_cascade(label="File", menu=file_m)

        file_m1 = Menu(menubar, tearoff=0)
        file_m1.add_command(label="Clear", command=new)
        file_m1.add_command(label="Cut")
        file_m1.add_command(label="Paste")
        menubar.add_cascade(label="Edit", menu=file_m1)

        name_l.destroy()
        age_l.destroy()
        DOB_l.destroy()
        gender_l.destroy()
        phone_l.destroy()
        subject_l.destroy()
        program_l.destroy()
        address_l.destroy()
        entry6.destroy()
        entry4.destroy()
        entry2.destroy()
        entry1.destroy()
        DOB_m.destroy()
        DOB_y.destroy()
        DOB_d.destroy()
        pro_l.destroy()
        s_1.destroy()
        s_2.destroy()
        s_3.destroy()
        c_button.destroy()
        s_button.destroy()
        s_button1.destroy()
        gender_m.destroy()
        gender_f.destroy()
        title_l.destroy()

        def back():
            notebook.destroy()
            menubar.destroy()
            main()

        button_back = Button(notebook, text="Back", font=font_2, bg="white", fg="black", command=back)
        button_back.place(x=300, y=300)

    
    def clear():
        entry1.delete(0, tkinter.END)
        entry2.delete(0, tkinter.END)
        entry4.delete(0, tkinter.END)
        entry6.delete(0, tkinter.END)
        s_1.deselect()
        s_2.deselect()
        s_3.deselect()
        g_f.set(None)
        DOB_d.delete(0, tkinter.END)
        DOB_m.delete(0, tkinter.END)
        DOB_y.delete(0, tkinter.END)
        pro_l.current(0)


    def submit():
        global all_entry
        com_sub = []
        if sub1.get() == 1:
            get1 = s_1.cget("text")
            com_sub.append(get1)
        if sub2.get() == 1:
            get2 = s_2.cget("text")
            com_sub.append(get2)
        if sub3.get() == 1:
            get3 = s_3.cget("text")
            com_sub.append(get3)
        if sub1.get() == 0 and sub2.get() == 0 and sub3.get() == 0:
            com_sub = "None"

        s_gender = g_f.get()
        name = entry1.get()
        age = entry2.get()
        phone = entry4.get()
        address = entry6.get()
        lang = pro_l.get()
        DOB_s = f"{DOB_d.get()}/{DOB_m.get()}/{DOB_y.get()}"
        all_entry = f"Name:{name}\nAge:{age}\nGender:{s_gender}\nDOB:{DOB_s}\nPhone:{phone}\nSubject:{com_sub}\nLanguage:{lang}\nAddress:{address}"
        


    g_f = tkinter.StringVar()
    sub1 = IntVar()
    sub2 = IntVar()
    sub3 = IntVar()


    title_l = Label(form, text="Form", font=font_2, bg="black", fg="white", padx=10, pady=5, relief="raised")
    title_l.pack()

    # lables
    name_l = Label(form, text="Name:", font=font_1, bg="#106EBE")
    name_l.place(x=100, y=120)
    age_l = Label(form, text="Age:", font=font_1, bg="#106EBE")
    age_l.place(x=100, y=160)
    gender_l = Label(form, text="Gender:", font=font_1, bg="#106EBE")
    gender_l.place(x=100, y=200)
    DOB_l = Label(form, text="DOB:", font=font_1, bg="#106EBE")
    DOB_l.place(x=100, y=240)
    phone_l = Label(form, text="Phone:", font=font_1, bg="#106EBE")
    phone_l.place(x=100, y=280)
    subject_l = Label(form, text="Subject:", font=font_1, bg="#106EBE")
    subject_l.place(x=100, y=320)
    program_l = Label(form, text="Language:", font=font_1, bg="#106EBE")
    program_l.place(x=100, y=360)
    address_l = Label(form, text="Address:", font=font_1, bg="#106EBE")
    address_l.place(x=100, y=400)
    
    # entry
    entry1 = Entry(form, width=20, font=font_1, bg="white", fg="black", relief="raised")
    entry1.place(x=200, y=120)
    entry2 = Entry(form, width=20, font=font_1, bg="white", fg="black", relief="raised")
    entry2.place(x=200, y=160)
    entry4 = Entry(form, width=20, font=font_1, bg="white", fg="black", relief="raised")
    entry4.place(x=200, y=280)
    entry6 = Entry(form, width=20, font=font_1, bg="white", fg="black", relief="raised")
    entry6.place(x=200, y=400)
    
    # checkbox-subject
    s_1 = Checkbutton(form, text="Tamil", variable=sub1, bg="#106EBE", fg="black", font=font_1, onvalue=1, offvalue=0)
    s_1.place(x=200, y=320)
    s_2 = Checkbutton(form, text="English", variable=sub2, bg="#106EBE", fg="black", font=font_1, onvalue=1, offvalue=0)
    s_2.place(x=300, y=320)
    s_3 = Checkbutton(form, text="Maths", variable=sub3, bg="#106EBE", fg="black", font=font_1, onvalue=1, offvalue=0)
    s_3.place(x=400, y=320)
    
    # gender
    gender_m = Radiobutton(form, text="Male", variable=g_f, value="Male")
    gender_m.place(x=200, y=200)
    gender_f = Radiobutton(form, text="female", variable=g_f, value="Female")
    gender_f.place(x=280, y=200)
    
    # spinbox
    DOB_d = Spinbox(form, from_=1, to=31, width=2, font=font_3)
    DOB_d.place(x=200, y=240)
    DOB_m = Spinbox(form, from_=1, to=12, width=2, font=font_3)
    DOB_m.place(x=240, y=240)
    DOB_y = Spinbox(form, from_=1980, to=2020, width=5, font=font_3)
    DOB_y.place(x=280, y=240)
    
    # combobox
    pro_l = ttk.Combobox(form, width=20, state="readonly")
    pro_l["values"] = ("C", "C++", "java", "python")
    pro_l.current(0)
    pro_l.place(x=200, y=360)
    
    s_button = Button(form, text="Submit", font=font_1, bg="white", fg="black", activebackground="black",
                      activeforeground="white", relief="raised", command=submit)
    s_button.place(x=200, y=440)
    c_button = Button(form, text="Cancel", font=font_1, bg="white", fg="black", activebackground="black",
                      activeforeground="white", relief="raised", command=clear)
    c_button.place(x=300, y=440)
    s_button1 = Button(form, text="Submit and Edit", font=font_1, bg="white", fg="black", activebackground="black",
                       activeforeground="white", relief="raised", command=submit_edit)
    s_button1.place(x=200, y=500)

    form.mainloop()

main()

import tkinter as tk
from tkinter import filedialog

class Notepad(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Notepad")
        self.text = tk.Text(self, wrap="word")
        self.text.pack(side="top", fill="both", expand=True)
        self.menu = tk.Menu(self)
        self.config(menu=self.menu)
        file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)
        edit_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Cut", command=self.cut)
        edit_menu.add_command(label="Copy", command=self.copy)
        edit_menu.add_command(label="Paste", command=self.paste)

    def new_file(self):
        self.text.delete("1.0", "end")
        self.title("Notepad")

    def open_file(self):
        file = filedialog.askopenfile(parent=self, mode="rb", title="Open a file")
        if file:
            contents = file.read()
            
            self.text.delete("1.0", "end")
            self.text.insert("1.0", contents)
            file.close()
            self.title(file.name + " - Notepad")

    def save_file(self):
        file = filedialog.asksaveasfile(mode="w", defaultextension=".txt", filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
        if file:
            contents = self.text.get("1.0", "end")
            file.write(contents)
            file.close()
            self.title(file.name + " - Notepad")

    def cut(self):
        self.text.event_generate("<<Cut>>")

    def copy(self):
        self.text.event_generate("<<Copy>>")

    def paste(self):
        self.text.event_generate("<<Paste>>")

if __name__ == "__main__":
    notepad = Notepad()
    notepad.mainloop()

from tkinter import *
from tkinter import messagebox

tk = Tk()
tk.geometry("500x500")
tk.title("sakthi")
def getdata():
    data = txtN.get()
    lab = Label(tk, text=data, font=("times", 20), fg="green")
    lab.pack()
    messagebox.showinfo("messagebox", data)
def clear():
    txtN.delete(0, END)

def reverse_delete():
    data = txtN.get()
    length = len(data)
    txtN.delete(length - 1, length)


txtN = Entry(tk, width=30, font=("times", 20), fg="black")
txtN.pack()


btn = Button(tk, text="submit", font=("times", 15), width=10, padx=30, pady=10, bg="green", fg="white", command=getdata)
btn.pack()


btn_clr = Button(tk, text="clear", font=("times", 15), width=10, padx=30, pady=10, bg="red", fg="white", command=clear)
btn_clr.pack()


reverse_btn = Button(tk, text="Reverse Delete", font=("times", 15), width=15, bg="blue", fg="white", command=reverse_delete)
reverse_btn.pack()

tk.mainloop()


import tkinter
from PIL import Image, ImageTk

root = tkinter.Tk()
root.title("Background Image")
root.geometry("1000x700")

image_path=r"C:\Users\user\Desktop\python web file\python web\class boot\flower\Coffee-Cup-Good-Morning-Image-Free-Download-for-Whatsapp.jpg"
image = Image.open(image_path)
bg_image = ImageTk.PhotoImage(image)


bg_label = tkinter.Label(root, image=bg_image)
bg_label.place(x=10,y=20)


label = tkinter.Label(root, text="Hello, Tkinter!", fg="white", font=("times", 20))
label.pack()


root.mainloop()



