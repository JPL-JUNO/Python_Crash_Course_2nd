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


class Battery:
    def __init__(self, battery_size=75):
        self.batter_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.batter_size}-kWh battery.")

    def get_range(self):
        if self.batter_size == 75:
            ranges = 260
        elif self.batter_size == 100:
            ranges = 315
        else:
            ranges = 0
        print(f"This car can go about {ranges} miles on a full charge.")

# class ElectricCar(Car):
#     def __init__(self, maker, model, year):
#         """
#         初始化父类的属性
#         :param maker: 制造商
#         :param model: 型号
#         :param year: 生产年份
#         """
#         super().__init__(maker, model, year)  # super()为特殊函数，可以调用父类（superclass）初始化函数
#         self.battery_size = 75  # 定义子类的属性
#
#     def describe_battery(self):  # 定义子类的属性
#         print(f"This car has a {self.battery_size}-kWh battery.")


class ElectricCar(Car):
    def __init__(self, maker, model, year):
        """
        初始化父类的属性
        :param maker: 制造商
        :param model: 型号
        :param year: 生产年份
        """
        super().__init__(maker, model, year)  # super()为特殊函数，可以调用父类（superclass）初始化函数
        self.battery_size = Battery()  # 定义子类的属性


# my_tesla = ElectricCar('tesla', 'model a', 2019)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery_size.describe_battery()
# my_tesla.battery_size.get_range()
