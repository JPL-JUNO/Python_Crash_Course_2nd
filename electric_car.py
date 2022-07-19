from car import Car


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


