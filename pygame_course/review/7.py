x = input("enter something: ")
c = 0
for char in x:
    if char in ("a", "e", "i", "o", "u"):
        c += 1
print(c)


لیست = []
تاپل = ()
for i in range(3):
    اسم = input("enter something:> ")
    لیست.append(اسم)
    if len(اسم) > 3:
        تاپل += (اسم,)
print(لیست)
print(تاپل)

my_tuple = ('sara','yasaman', 'ali', 'nikan', 'amir')
largest = my_tuple[0]
for name in my_tuple:
    if len(name) > len(largest):
        largest = name
print(largest)
        