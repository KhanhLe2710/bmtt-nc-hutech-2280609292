my_list = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]
mixed_list = [10, "hello", 3.14, True]

print(my_list[0])
print(names[2])

my_list[1] = 20
print(my_list)

names.append("David")
print(names)

del my_list[2]
print(my_list)

for element in names:
    print(element)