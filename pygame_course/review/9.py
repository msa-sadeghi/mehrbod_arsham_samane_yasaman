# import time
# message = "hello"


# for c in message:
#     print(c, end="", flush=True)
#     time.sleep(0.2)

# students_score = {
#     "s1" : 90,
#     "s2" : 100,
#     "s3" : 89,
#     "s4" : 95
# }
# counter = 0
# for i in students_score:
#     if students_score[i] > 90:
#         print(i)
#         counter += 1
# print(counter)
# students_score["25"] = 78
# students_score.update({"s6" : 86})

numbers = input("enter three numbers: (1-2-3)")
print(numbers.split("-"))
s = 0
for num in numbers.split("-"):
    s+= int(num)
print(s)
    