# students = []

# print(students)
# students.append("sorena")
# print(students)
# students.append("mehrbod")
# print(students)
# students.append("arsham")
# print(students)
# students.append("samane")
# print(students)
# print(len(students))

# students = []

# for i in range(4):
#     new_name = input("enter a name: ")
#     students.append(new_name)

# print(students)

# TODO
"""
با کمک حلقه فور برنامه ای بنویسید که پنج عدد از ورودی دریافت نماید
و عددهای زوج را داخل یک لیست و
عددهای فرد را داخل لیست دیگری ذخیره کند

"""
"""
راهنمایی: تشخیص زوج و یا فرد بودن عدد
n = int(input("> "))
if n % 2 == 0:
    print("even")
else:
    print("odd")

"""

foods = ["mashroom","pizza","blalal"]
foods[0] = "banana"
print(foods[0])
print(foods[1])
print(foods[2])
print(foods[-1])
print(foods[len(foods)-1])

foods.remove("blalal")
print(foods)

del foods[0]
print(foods)