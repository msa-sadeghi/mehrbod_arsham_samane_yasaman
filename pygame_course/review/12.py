from tkinter import *

def my_function():
    my_label.config(fg="red")
    label2.config(fg="green")

window = Tk()
my_label = Label(window, text="سلام به همه. اینجا کلاس پایتونه")
my_label.pack()

label2 = Label(window, text="این جلسه برنامه گرافیکی ساخته می شود")
label2.pack()

my_button = Button(window, text="کلیک کن", command=my_function)
my_button.pack()
# تمرین
# یک دکمه اضافه کنید که با فشردن آن رنگ پس زمینه برچسب اول و دوم به رنگ دلخواه تغییر نماید
# bg   رنگ پس زمینه
window.mainloop()