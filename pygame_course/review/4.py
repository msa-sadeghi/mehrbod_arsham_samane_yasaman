# x = [1,2,3,4]
# x.append(5)
# print(x)
# x.insert(0, 6)
# print(x)
# y = [11,12,13,14,15]
# x.extend(y)
# print(x)
# print(x.remove(11))
# print(x)
# print(x.count(11))
# x.reverse()
# print(x)
# x.sort()
# print(x)
# print(x.index(15))
# x.pop()
# print(x)
# names = ["yasaman", "samane", "arsham", "mehrbod"]
# names.sort()
# print(names)

# x = [True, False, True]
# x.sort()
# print(x)

# x = {
#     'red':"ali",
#     'green':"sara"
# }
# print(x['red'])
# print(x['green'])

# x['yellow'] = "artin"
# print(x)
# print(x['yellow'])

# five color  =>  sort    len    count "red"

# for   ->   5   name   +   food   => dictionary 

# f = {}
# for i in range(5):
#     name = input("enter a name: ")
#     food = input("enter a food name: ")
#     f[name] = food
    
# print(f)


# x = [[1,2,3], [4,5,6]]
# s = 0
# for i in range(len(x)):
#     for j in range(len(x[i])):
#         s += x[i][j]
# print(s)       


students_scores = [["roze", 12], ["matin", 13], ["artin", 15], ["sara", 20]]
# برنامه ای بنویسید که مجموع نمرات دانش آموزان موجود در لیست بالا را محاسبه و نمایش دهد
# a = 0
# for item in students_scores:
#     a += item[1]
# print(a)

# برنامه ای بنویسید که میانگین نمرات موجود در لیست بالا را محاسبه و نمایش دهد.
# میانگین یعنی جمع نمرات تقسیم بر تعدادشان
# a = 0
# for item in students_scores:
#     a += item[1]
# print(a/len(students_scores))


# برنامه ای بنویسید که از بین دانش آموزان لیست بالا بالاترین نمره و نیز پائین ترین نمره را پیدا نماید
# students_scores = [["roze", 12], ["matin", 13], ["artin", 15], ["sara", 20]]

# max_score = students_scores[0][1]
# min_score = students_scores[0][1]
# name = ""
# for student in students_scores:
#     if student[1] > max_score:
#         max_score = student[1]
#         name = student[0]
        
#     if student[1] < min_score:
#         min_score = student[1]
        
# print("max score is", max_score, "student name is", name)
# print("min score is", min_score)


# students_scores = [["roze", 12], ["matin", 13], ["artin", 15], ["sara", 20]]
# students_scores[1][0] = "armin"
# print(students_scores)
# del students_scores[0]
# students_scores[2][1] = 19
# print(students_scores)

# name = input("enter a name: ")
# score = int(input("enter score: "))
# students_scores.append([name, score])
# print(students_scores)

# و اسم کسی که بالاترین نمره را آورده است نیز نمایش دهد
# در تمام این تمرینات می بایست از حلقه استفاده کنید
# برنامه ای بنویسید که از لیست بالا اسم
# matin
# را به
# armin
# تغییر دهد
# برنامه ای بنویسید که رز و نمره او را از لیست حذف نماید
# برنامه ای بنویسید که نمراه سارا را به نوزده تغییر دهد
# برنامه ای بنویسید که اسم و نمره فردی را از ورودی دریفات نماید و به لیست بالا اضافه کند
# del students_scores[0]
# students_scores.pop(0)
####################################################
# x = [[1,2,3,4,5,100,101], [2,4,3,77,54,89], [54,11,23,0, 98]]
# برنامه ای بنویسید ک هاعداد زوج موجود در لیست بالا را با هم جمع نماید و حاصل را نمایش دهد
# عدد زوج عددی است که باقیمانده تقسیم آن بر دو صفر باشد
# حتما از حلقه استفاده نماید
# s = 0
# for item in x:
#     for num in item:
#         if num % 2 == 0:
#             s += num
            
# print(s)
            
    