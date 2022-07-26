import json


def get_sorted_username():
    """
    如果存储了用户名，就获取它。
    :return:
    """
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """
    提示用户输入用户名
    :return:
    """
    username = input('What is your name? ')
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """
    问候用户，并指出名字
    :return:
    """
    username = get_sorted_username()
    if username:
        print(f'Welcome back, {username}!')
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")


greet_user()
