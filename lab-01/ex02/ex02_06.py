x = 10
if x > 5:
    print("x lớn hơn 5")
elif x == 5:
    print("x bằng 5")
else:
    print("x nhỏ hơn 5")

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

count = 0
while count < 5:
    print(count)
    count += 1

for i in range(1, 101):
    if i % 5 == 0:
        print("Số chia hết cho 5 đầu tiên là:", i)
        break

for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i)

x = 5
if x > 10:
    print("x lớn hơn 10")
else:
    pass