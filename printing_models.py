def print_models(unprinted_designs, completed_models):
    """

    :param unprinted_designs:
    :param completed_models:
    :return:
    """
    while unprinted_designs:
        current_model = unprinted_designs.pop()
        print(f'Printing_model: {current_model}')
        completed_models.append(current_model)


def show_completed_models(completed_models):
    """

    :param completed_models:
    :return:
    """
    print('\nThe following models have been printed:')
    for completed_model in completed_models:
        print(completed_model)


unprinted_models = ['phone', 'robot pendant', 'dodecaherdron']
completed_models = []

print_models(unprinted_models, completed_models)
show_completed_models(completed_models)
print(unprinted_models)

unprinted_models = ['phone', 'robot pendant', 'dodecaherdron']
completed_models = []

# 使用[:]创建列表的副本，将列表的副本传递给函数，列表本身禁止修改，可用于备份数据以备查看
print_models(unprinted_models[:], completed_models)
show_completed_models(completed_models)
print(unprinted_models)
