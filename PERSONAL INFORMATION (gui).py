from tkinter import *
window = Tk()
window.geometry('380x300')
window.config(bg='gray')
window.resizable(0, 0)
window.title("Personal Information")
title = Label(window, text= "Personal Information", padx=30, pady=10, font=("times", 12), bg='black', fg='white')
title.pack(fill=X)
window.update()
Label(window, text='Name :', bg='gray', fg='white').place(x=10, y=50)
name_box = Text(window, height=1, width=30, font=("times", 12), bg='gray', fg='white')
name_box.place(x=60, y=52)
Label(window, text="Date Of Birth :", bg='gray', fg='white').place(x=10, y=85)
dob = Text(window, height=0.5, width=20, font=("times", 12), bg='gray', fg='white')
dob.place(x=100, y=87)
Label(window, text="Blood Group :", bg='gray', fg='white').place(x=10, y=120)
blood =Text(window, height=0.5, width=10, font=("times", 12), bg='gray', fg='white')
blood.place(x=100, y=122)
Label(window, text="Address :", bg='gray', fg='white').place(x=10, y=160)
address = Text(window, height=2, width=35, font=('times', 12), bg='gray', fg='white')
address.place(x=75, y=162)
Label(window, text="Contact Number :", bg='gray', fg='white').place(x=10, y=225)
cn = Text(window, height=0.5, width=20, bg='gray', fg='white', font=('times', 12))
cn.place(x=120, y=227)

data = open("Info.txt", 'a')


def main():
    entry_1 = name_box.get(1.0, END)
    e1 = str(entry_1)
    entry_2 = dob.get(1.0, END)
    e2 = str(entry_2)
    entry_3 = blood.get(1.0, END)
    e3 = str(entry_3)
    entry_4 = address.get(1.0, END)
    e4 = str(entry_4)
    entry_5 = cn.get(1.0, END)
    e5 = str(entry_5)
    data.write('_'*100+ '\n'+ 'Name : '+ e1+ 'Date Of Birth : '+ e2+
               'Blood Group : '+ e3+ 'Address : '+ e4+ 'Contact Number : '+e5)
    Label(window, text='Recorded', font=('times', 10), bg='gray', fg='white').place(x=170, y=275)
    window.update()


def exit():
    window.destroy()


start = Button(window, text='Record', command=main, width=10, font='times',
               bg='light green', activebackground='cyan').place(x=50, y=265)
close = Button(window, text='Close', command=exit, width=10, font='times',
               bg='red', activebackground='orange').place(x=245, y=265)

window.mainloop()
