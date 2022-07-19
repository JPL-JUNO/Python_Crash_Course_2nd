def get_formatted_name(first_name, last_name):
    """
    返回整洁的姓名全称
    :param first_name: 名
    :param last_name: 姓
    :return:
    """
    full_name = f'{first_name} {last_name}'
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)


def get_formatted_name(first_name, last_name, middle_name=''):
    """
    输出姓名全称
    :param first_name: 名
    :param last_name: 姓
    :param middle_name: 中间名
    :return: 返回姓名的全称并实现首字母大写
    """
    if middle_name:
        full_name = f'{first_name} {middle_name} {last_name}'
    else:
        full_name = f'{first_name} {last_name}'
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)