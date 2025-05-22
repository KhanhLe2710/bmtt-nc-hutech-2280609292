class Car:
    def _init_(self, brand, model):
        self.brand = brand
        self.model = model
    
    def get_info(self):
        return f"{self.brand} {self.model}"
my_car = Car("Toyota", "Corolla")
print(my_car.get_info())