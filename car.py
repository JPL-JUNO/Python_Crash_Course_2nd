class Car:
    def __init__(self, maker, model, year):
        self.maker = maker
        self.model = model
        self.year = year
        self.odometer_reading = 0   # 给Car类添加属性，但是不需要在实例化的时候赋予

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.maker} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()
#
# my_new_car.odometer_reading = 27    # 直接修改参数值
# print(my_new_car.get_descriptive_name())
#
# my_new_car.update_odometer(36)  # 调用类中定义的更新函数来修改里程值
# my_new_car.read_odometer()
#
# my_used_car = Car('subaru', 'outback', 2015)
# print(my_used_car.get_descriptive_name())
#
# my_used_car.read_odometer()
#
# my_used_car.update_odometer(23_500)   # 23_500表示23500
# my_used_car.read_odometer()
#
# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()
