def bulid_profile(first, last, **user_info):
    """

    :param first:
    :param last:
    :param user_info:
    :return:
    """
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = bulid_profile('albert',
                             'einstein',
                             location='princeton',
                             filed='physics')

print(user_profile)


