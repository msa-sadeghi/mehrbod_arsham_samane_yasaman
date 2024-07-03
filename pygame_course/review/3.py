# x = "a"

# print(ord(x))

# print(chr(97))

# A = [
#     ["mehrbod", "yasaman"],
#     ["samane", "arsham"]
#     ]

# print(A[0][0], end="   ")
# print(A[0][1])
# print(A[1][0], end="   ")
# print(A[1][1])

# برنامه ای بنویسید که مجموع اعداد موجود در لیست دو بعدی یا ماتریس زیر را نمایش دهد
A = [
     [1,20,30],
     [2,10,100],
     [23,19,8]
     ]
x = A[0][0] + A[0][1] + A[0][2] + A[1][0] + A[1][1] + A[1][2] + A[2][0] + A[2][1] + A[2][2]
print(x)


def my_function(M):
     s = 0
     for i in range(len(M)):
          for j in range(len(M[i])):
               s += M[i][j]
     return s
print(my_function(A))
               
          