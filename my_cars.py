# 从一个模块导入多个类
# from ElectricCar import Car, ElectricCar
# 导入整个模块
# import ElectricCar
# 在一个模块中导入另一个模块
from car import Car
from electric_car import ElectricCar
# 使用别名
# from electric_car import ElectricCar as EC
#
my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
