# 传递任意数量的实参
# def make_pizza(*toppings):  # 创建空元组
#     """
#     打印顾客的配料表
#     :param toppings:
#     :return:
#     """
#     print('\nMaking a pizza with the following toppings:')
#     for topping in toppings:
#         print(f'-- {topping}')
#
#
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')


def make_pizza(size, *toppings):  # 接收任意实参的形参必须放在最后
    """
    打印顾客的配料表
    :param size:
    :param toppings:
    :return:
    """
    print(f'\nMaking a {size}-inch pizza with the following toppings:')
    for topping in toppings:
        print(f'-- {topping}')


# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
