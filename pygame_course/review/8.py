# sports = ["football", "tennis"]
# f = {
#     'nikan' : 'football',
#     'sara': 'tennis'
# }

# print("nikan likes", f['nikan'])
# print("sara likes", f['sara'])


ages = ()
for i in range(5):
    a = int(input("enter an age: "))
    ages += (a,)
# print(sum(ages))
s = 0
for a in ages:
    s += a
print(s)

ages = []
for i in range(5):
    a = int(input("enter an age: "))
    ages.append(a)
ages = tuple(ages)
