
# name = input("Please enter your name: ")
# print('\nHello, {}'.format(name))
#
# prompt = 'If you tell us who you are, we can personalize the messages you see.'
# prompt += '\nWhat is your first name? '
#
# name = input(prompt)
# print(f'\nHello, {name}')

# 8.1 定义函数
def greet_user():
    """
    简单的问候语
    """
    print("Hello!")


greet_user()


def greet_user(username):
    """
    简单的问候语
    """
    print(f"Hello, {username.title()}!")


greet_user("Stephen CUI")


# 8.3
def get_formatted_name(first_name, last_name):
    """
    实现用户输入的姓名全称
    :param first_name: 名
    :param last_name: 姓
    :return: 姓名全称
    """
    full_name = f'{first_name} {last_name}'
    return full_name


while True:
    print('\nPlease tell me your name:')
    print('enter "q" at any time to quit')
    
    f_name = input('First_name: ')
    if f_name == 'q':
        break
    l_name = input('Last_name: ')
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f'\nHello, {formatted_name}!')