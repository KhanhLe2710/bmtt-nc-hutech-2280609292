my_dict = {}
person = {"name": "Alice", "age": 25, "city": "New York"}

print(person["name"])
print(person["age"])

person["email"] = "alice@example.com"
person["age"] = 26

del person["city"]
age = person.pop("age")

print(person.keys())
print(person.values())
print(person.items())