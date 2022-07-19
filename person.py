def build_person(first_name, last_name, age=None):
    """
    实现包含人物姓名的功能
    :param age: 年龄
    :param first_name: 名
    :param last_name: 姓
    :return: 字典
    """
    person = {'first_name': first_name, 'last_name': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix', 37)
print(musician)
