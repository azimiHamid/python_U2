names = ["Hamid", "hadi", "habib", "haji", "yasin", "abbas", "Ali", "Mohammad", "Ahmad", "Adil", "Mustafa", "Murtaza", "khaliq", "Hasib", "Ahmadullah", "Jawid", "Navid", "Nasrat", "Sami", "Samir"]

numbers = [1,2,3,4,5,6,7,8,9,10]

# Numbers less than 5
less_than_5 = [num for num in numbers if num < 5]
print(less_than_5)


# names less than 5 characters
new_names = [name for name in names if len(name) < 5]
print(new_names)

uppercase_names = [name.upper() for name in names if len(name) >= 8]
titlecase_names = [name.title() for name in names]

print(uppercase_names)



# EXERCISE OF LIST COMPRIHENSION: Data overlap
# 1. Read numbers from file1.txt and file2.txt
with open("./utils_26/file1.txt") as f1, open("./utils_26/file2.txt") as f2:
    file1 = [int(item.strip()) for item in f1.readlines()]
    file2 = [int(item.strip()) for item in f2.readlines()]

# 2. Find the intersection of both list and create another list from it
result = [num for num in file1 if num in file2]
print(result)
