# for i in range(5):
#     print("hello")


# i = 0
# while i < 5:
#     print("hello")
#     i += 1


# run = True
# while run:
#     print("hello")
#     x = input("do you want to quit?(y or n): ")
#     if x == "y":
#         break

# def average(n1, n2, n3):
#     return (n1 + n2 + n3)//3


# print(average(20,25,32))


# TODO  تابعی بنویسید که پنج عدد از ورودی دریافت نماید
# و اعداد فرد وارد شده را با هم جمع نماید و حاصل جمع را برگرداند

# def greet(name, family):
#     return f"{name} {family}, welcome to our class."

# print(greet("artin","blalalal"))

def add_odd_numbers(x,y,z,w,k):
    total = 0
    if x % 2 != 0:
        total += x
    if y % 2 != 0:
        total += y
    if z % 2 != 0:
        total += z
    if w % 2 != 0:
        total += w
    if k % 2 != 0:
        total += k
    return total


res = add_odd_numbers(1,2,3,4,5)
print(res)






def add_odd_numbers():
    total = 0
    for i in range(5):
        x = int(input("enter a number: "))
        if x % 2 != 0 :
            total += x

    return total


print(add_odd_numbers())


def add_odd_numbers(x):
    total = 0
    for number in x:
        if number % 2 != 0:
            total += number
    return total

print(add_odd_numbers([1,2,3,4,5]))