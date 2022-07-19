def get_formatted_name(first_name, last_name, middle_name=''):
    """
    生成整洁的姓名
    :param middle_name:
    :param first_name:
    :param last_name:
    :return:
    """
    if middle_name:
        full_name = f'{first_name} {middle_name} {last_name}'
    else:
        full_name = f'{first_name} {last_name}'
    return full_name.title()
