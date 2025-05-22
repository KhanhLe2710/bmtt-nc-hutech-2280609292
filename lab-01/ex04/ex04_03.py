class ClassName:
    class_attribute = "Class Attribute"

    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

# Tạo đối tượng từ lớp
value1 = "Hello"
value2 = "World"
object_name = ClassName(value1, value2)

# In ra các thuộc tính
print(object_name.attribute1)  # Hello
print(object_name.attribute2)  # World
print(ClassName.class_attribute)  # Class Attribute
