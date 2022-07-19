import pizza
import pizza as p  # 给模块指定别名
from pizza import make_pizza  # 显示调用了函数
from pizza import make_pizza as mp  # 使用别名
from pizza import *  # 如果遇到同名函数，将会产生意想不到的结果

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
