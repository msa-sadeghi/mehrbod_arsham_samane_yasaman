name = input("enter a name: ")
age = int(input("enter your age: "))

if age <= 6:
    print(f"{name}, you are kid and you can't go to school.")
elif age > 6 and age <= 18:
    print(f"{name}, you can go to school.")
else:
    print(f"{name}, you are old and you can't go to school.")

# TODO
"""
برنامه ای بنویسید که
نام و نمرات سه درس یک دانش آموز را از ورودی دریافت نماید
و معدل او را حساب کند
معدل یعنی مجموع نمرات تقسیم بر تعدادشان
اگر معدل دانش آموز از نوزده بیشتر بود
A
را پرینت کند
اگر معدل از 18 بیشتر بود
B
را 
و اگر معدل از 17 بیشتر بود
C
و در غیراینصورت 
D 
را پرینت نماید

"""
