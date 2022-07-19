def greet_users(names):
    """
    按个返回列表中的姓名
    :param names: 用户名列表
    :return: 暂无返回值
    """
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)


username = ['hannah', 'ty', 'margot']
greet_users(username)