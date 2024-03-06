# favorite_foods = {}

# for i in range(2):
#     name = input('enter a name: ')
#     food = input('enter a food: ')
#     favorite_foods[name] = food


# name = input('enter a name: ')
# print(favorite_foods[name])



# print(favorite_foods)

# name = "nima"
# print(name[0])

numbers = [1,2,3,4,5,6,7,8,9]
print(numbers[0])
print(numbers[1])
for n in numbers:
    print(n)

for i in range(len(numbers)):
    print(numbers[i])

numbers = []

for i in range(4):
    n = int(input("enter a number: "))
    numbers.append(n)

for i in range(0, len(numbers), 2):
    print(numbers[i])